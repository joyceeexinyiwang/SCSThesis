"""

"""

import datetime, time, sys, json, os
import tweepy
from tools import rest_tools as rest
from tools import general_tools as gen

def isRelatedToAgency(api, tweet, agency_handle):

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
		(result, accum) = isRelatedToAgency(api, tweet["retweeted_status"], agency_handle)
		if result:
			accum.append(json.dumps(tweet))
			return (True, accum)
		addAccum.extend(accum)

	if "quoted_status" in tweet:
		(result, accum) = isRelatedToAgency(api, tweet["quoted_status"], agency_handle)
		if result:
			accum.append(json.dumps(tweet))
			return (True, accum)
		addAccum.extend(accum)

	if tweet["in_reply_to_status_id"] != None:
		reply_to = None
		try:
			reply_to = api.get_status(id=tweet["in_reply_to_status_id"], tweet_mode='extended')
		except:
			print("get_status error with id=" + tweet["in_reply_to_status_id_str"])

		if (reply_to != None):
			(result, accum) = isRelatedToAgency(api, reply_to._json, agency_handle)
			if result:
				accum.append(json.dumps(tweet))
				return (True, accum)
			addAccum.extend(accum)

	return (False, addAccum)

def profileAgent(api, tweet): # very naive measurement of agent influence
	user = tweet["user"]
	profile = {}
	profile["user_object"] = user
	profile["influence"] = None # high, mid, low, vlow (suspiciously low)
	profile["activeness"] = None # inactive, active, veryactive
	profile["profession"] = None # currently: journalism, other (future: journalist, newsagency, citizen, bot)
	
	# Influence (TO-DO: include centrality measures, inward v.s. outward influence)
	sphere = user["followers_count"] + user["friends_count"]
	if sphere < 200:
		profile["influence"] = "vlow"
	elif sphere < 2000:
		profile["influence"] = "low"
	elif sphere < 10000:
		profile["influence"] = "mid"
	else:
		profile["influence"] = "high"

	# Activeness: number of times that the user tweeted in the past 30 days of the event 
	user["statuses_count"]
	user["favourites_count"]
	timeline = gen.getTimeline(user["id"]) # check if the user has been active recently, in respect to the date of event
	activeCounts = 0
	for tweet in timeline:
		dateList = tweet["created_at"].split(" ") # twitter time stamp format: "Sun Nov 04 19:43:10 +0000 2018"
		date = datetime.date(int(dateList[-1]), montoNum(dateList[1]), int(dateList[2]))
		if datetime.date(2018, 11, 7) - date < timedelta(days=30): 
			activeCounts += 1
	if activeCounts < 10: # completely arbitrary
		profile["activeness"] = "inactive"
	elif activeCounts < 50:
		profile["activeness"] = "active"
	else:
		profile["activeness"] = "very_active"

	# Profession (TO-DO: user["verified"], is bot?, news agency detection)
	newskeywords = ["news", "newsroom", "columnist", "journalist", "reporter"]
	profile["profession"] = "other"
	for w in newskeywords:
		if w in user["description"]:
			profile["profession"] = "journalism"

	return profile


def getRetweets(api, output_path, maxTweets, tweet_segment, tweet_id):

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

	writeFile(output_path, str(tweet_id) + "_retweets.json", retweets)

	return retweets

def getQuotes(api, output_path, maxTweets, tweet_url, tweet_id):

	print("Getting Quotes for id=" + str(tweet_id))


	# STEP 1: scrape using tweet url
	possible_quotes = rest.rest_scrape_single(tweet_url, maxTweets, api)

	# STEP 2: filter by quote status

	quotes = list(filter(lambda q: "quoted_status" in q._json and q._json["quoted_status"]["id"] == tweet_id, possible_quotes))
	quotes = list(map(lambda t: json.dumps(t._json), quotes))

	if not os.path.exists(output_path):
		os.makedirs(output_path)  

	writeFile(output_path, str(tweet_id) + "_quotes.json", quotes)

	return quotes


def getRepliesAndOthers(api, output_path, maxTweets, account_handle, tweet_id):

	print("Getting Replies and Others for id=" + str(tweet_id))

	# STEP 1: scrape all with news corp handle
	possible_related = rest.rest_scrape_single("@"+account_handle, maxTweets, api)

	# STEP 2: filter by reply status, recursively
	related = []
	add_ids = set()
	for r in related:
		if isRelatedToTweet(api, r._json, tweet_id):
			related.append(tweet)
			add_ids.add(tweet['id'])

	related = list(map(lambda t: json.dumps(t._json), related))

	if not os.path.exists(output_path):
		os.makedirs(output_path)  

	writeFile(output_path, str(tweet_id) + "_replies_others.json", related)

	return related

def isRelatedToTweet(api, tweet, tweet_id):
	if tweet["id"] == tweet_id:
		return True

	if "retweeted_status" in tweet:
		result = isRelatedToTweet(api, tweet["retweeted_status"], tweet_id)
		if result:
			return True

	if "quoted_status" in tweet:
		result = isRelatedToTweet(api, tweet["quoted_status"], tweet_id)
		if result:
			return True

	if tweet["in_reply_to_status_id"] != None:
		reply_to = None
		try:
			reply_to = api.get_status(id=tweet["in_reply_to_status_id"], tweet_mode='extended')
		except:
			print("get_status error with id=" + tweet["in_reply_to_status_id_str"])

		if (reply_to != None):
			result = isRelatedToTweet(api, reply_to._json, tweet_id)
			if result:
				return True

	return False


def writeFile(path, filename, tweets):
	if len(tweets) == 0:
		return

	o_file = open(path + "/" + filename, "w")
	o_file.write("\n".join(tweets))
