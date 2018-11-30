"""
"""

import datetime, time, sys, json, os, re
import tweepy
import pandas as pd
from textblob import TextBlob
from tools import rest_tools as rest
from tools import general_tools as gen


class NewsTools():

	def __init__(self, api):
		with open("tools/newsagents.csv") as i_file:
			alist = i_file.read()
		self.agencies = alist.split(",")
		self.api = api

	def isRelatedToAgency(self, tweet, agency_handle):

		addAccum = []

		if tweet["user"]["screen_name"] == agency_handle:
			# this tweet is tweeted by the news agency originally
			return (True, [json.dumps(tweet)])

		try:
			# this tweet contains a link to a news article by this agency
			if agency_handle in tweet["entities"]["urls"][0]["expanded_url"]:
				return (True, [json.dumps(tweet)])
			if agency_handle == "nytimes":
				if "nyti" in tweet["entities"]["urls"][0]["expanded_url"]:
					return (True, [json.dumps(tweet)])
		except:
			pass

		if "retweeted_status" in tweet:
			(result, accum) = self.isRelatedToAgency(tweet["retweeted_status"], agency_handle)
			if result:
				accum.append(json.dumps(tweet))
				return (True, accum)
			addAccum.extend(accum)

		if "quoted_status" in tweet:
			(result, accum) = self.isRelatedToAgency(tweet["quoted_status"], agency_handle)
			if result:
				accum.append(json.dumps(tweet))
				return (True, accum)
			addAccum.extend(accum)

		if tweet["in_reply_to_status_id"] != None:
			reply_to = None
			try:
				reply_to = self.api.get_status(id=tweet["in_reply_to_status_id"], tweet_mode='extended')
			except:
				print("get_status error with id=" + tweet["in_reply_to_status_id_str"])

			if (reply_to != None):
				(result, accum) = self.isRelatedToAgency(reply_to._json, agency_handle)
				if result:
					accum.append(json.dumps(tweet))
					return (True, accum)
				addAccum.extend(accum)

		return (False, addAccum)

	def opinionScore(self, tweet):
		full_text = tweet["full_text"]

		# To assess the **opinion strength** of the message you could use these indicators
			# a) use of emotional words (using code from Dave's script, tools/sentiment.py)
			# b) all cap words
			# d) use of exclamation points    	

		# ref: https://regex101.com/r/nG1gU7/609
		sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s", full_text)
		exclamation = full_text.count("!")
		totalSentences = len(sentences)

		words = re.split('; |, |\*|\n| |! |\!|\?|\.', "Today is good right.") # TO-DO: messed up by urls in tweets
		allCaps = len(list(filter(lambda w: w.isupper(), words)))
		totalWords = len(words)

		t = TextBlob(full_text)

		score = 0.0
		score += abs(t.sentiment.polarity) #0.0-1.0
		if exclamation > 0:
			if allCaps > 0:
				score += exclamation/totalSentences / 4 #0.0-0.25
				score += allCaps/totalWords / 4 #0.0-0.25
				score /= 1.5
			else:
				score += exclamation/totalSentences / 4 #0.0-0.25
				score /= 1.25
		else:
			if allCaps > 0:
				score += allCaps/totalWords / 4 #0.0-0.25
				score /= 1.25

		return score


	def profileAgent(self, tweet): # very naive measurement of agent influence
		user = tweet["user"]
		profile = {}
		profile["handle"] = user["screen_name"]
		profile["user_object"] = user
		profile["influence"] = None # high, mid, low, vlow (suspiciously low)
		profile["activeness"] = None # inactive, active, veryactive
		profile["profession"] = None # currently: journalism, other (future: journalist, newsagency, citizen, bot)
		
		# Influence (TO-DO: include centrality measures, inward v.s. outward influence)
		sphere = user["followers_count"] + user["friends_count"]
		if sphere < 200:
			profile["influence"] = "min"
		elif sphere < 8000:
			profile["influence"] = "low"
		elif sphere < 20000:
			profile["influence"] = "mid"
		else:
			profile["influence"] = "high"

		# Activeness: number of times that the user tweeted in the past 30 days of the event 
		# user["statuses_count"]
		# user["favourites_count"]
		timeline = gen.getTimeline(user["id"]) # check if the user has been active recently, in respect to the date of event
		activeCounts = 0
		for tweet in timeline:
			dateList = tweet["created_at"].split(" ") # twitter time stamp format: "Sun Nov 04 19:43:10 +0000 2018"
			date = datetime.date(int(dateList[-1]), gen.montoNum(dateList[1]), int(dateList[2]))
			if datetime.date(2018, 11, 7) - date < datetime.timedelta(days=30): 
				activeCounts += 1
		if activeCounts < 10: # <- completely arbitrary number
			profile["activeness"] = "inactive"
		elif activeCounts < 50:
			profile["activeness"] = "active"
		else:
			profile["activeness"] = "very_active"

		# Profession (TO-DO: user["verified"], is bot?, news agency detection)
		if self.isNewsProfessional(user["screen_name"]):
			profile["profession"] = "journalism"
		else:
			profile["profession"] = "unknown"


		return profile


	# def profileTweet(tweet):

	def isNewsProfessional(self, handle):
		# TO-DO
		return (handle in self.agencies)


	def getRetweets(self, output_path, maxTweets, tweet_segment, tweet_id):

		print("Getting Retweets for id=" + str(tweet_id))

		# STEP 1: scrape using tweet url
		possible_retweets = rest.rest_scrape_single("\"" + tweet_segment + "\"", maxTweets, api)

		# STEP 2: filter by retweet status
		retweets = []
		for rt in possible_retweets:
			if "retweeted_status" in rt._json and rt._json["retweeted_status"]["id"] == tweet_id:
				retweets.append(rt)

		retweets = list(map(lambda t: json.dumps(t._json), retweets))

		if not os.path.exists(output_path):
			os.makedirs(output_path)  

		self.writeFile(output_path, str(tweet_id) + "_retweets.json", retweets)

		return retweets

	def getQuotes(self, output_path, maxTweets, tweet_url, tweet_id):

		print("Getting Quotes for id=" + str(tweet_id))


		# STEP 1: scrape using tweet url
		possible_quotes = rest.rest_scrape_single(tweet_url, maxTweets, api)

		# STEP 2: filter by quote status

		quotes = list(filter(lambda q: "quoted_status" in q._json and q._json["quoted_status"]["id"] == tweet_id, possible_quotes))
		quotes = list(map(lambda t: json.dumps(t._json), quotes))

		if not os.path.exists(output_path):
			os.makedirs(output_path)  

		self.writeFile(output_path, str(tweet_id) + "_quotes.json", quotes)

		return quotes


	def getRepliesAndOthers(self, output_path, maxTweets, account_handle, tweet_id):

		print("Getting Replies and Others for id=" + str(tweet_id))

		# STEP 1: scrape all with news corp handle
		possible_related = rest.rest_scrape_single("@"+account_handle, maxTweets, api)

		# STEP 2: filter by reply status, recursively
		related = []
		add_ids = set()
		for r in related:
			if self.isRelatedToTweet(r._json, tweet_id):
				related.append(tweet)
				add_ids.add(tweet['id'])

		related = list(map(lambda t: json.dumps(t._json), related))

		if not os.path.exists(output_path):
			os.makedirs(output_path)  

		self.writeFile(output_path, str(tweet_id) + "_replies_others.json", related)

		return related

	def isRelatedToTweet(self, tweet, tweet_id):
		if tweet["id"] == tweet_id:
			return True

		if "retweeted_status" in tweet:
			result = self.isRelatedToTweet(tweet["retweeted_status"], tweet_id)
			if result:
				return True

		if "quoted_status" in tweet:
			result = self.isRelatedToTweet(tweet["quoted_status"], tweet_id)
			if result:
				return True

		if tweet["in_reply_to_status_id"] != None:
			reply_to = None
			try:
				reply_to = self.api.get_status(id=tweet["in_reply_to_status_id"], tweet_mode='extended')
			except:
				print("get_status error with id=" + tweet["in_reply_to_status_id_str"])

			if (reply_to != None):
				result = self.isRelatedToTweet(reply_to._json, tweet_id)
				if result:
					return True

		return False


	def writeFile(self, path, filename, tweets):
		if len(tweets) == 0:
			return

		o_file = open(path + "/" + filename, "w")
		o_file.write("\n".join(tweets))
