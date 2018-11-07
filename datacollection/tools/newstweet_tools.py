"""

"""

import datetime, time, sys, json, os
import tweepy
from tools import rest_tools as rest

def isRelatedToAgency(api, tweet, agency_handle):

	if tweet["user"]["screen_name"] == agency_handle:
		return (True, [json.dumps(tweet)])

	if "retweeted_status" in tweet:
		(result, accum) = isRelatedToAgency(api, tweet["retweeted_status"], agency_handle)
		if result:
			accum.append(json.dumps(tweet))
			return (True, accum)

	if "quoted_status" in tweet:
		(result, accum) = isRelatedToAgency(api, tweet["quoted_status"], agency_handle)
		if result:
			accum.append(json.dumps(tweet))
			return (True, accum)

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

	return (False, None)


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
		if isRelated(api, r._json, tweet_id):
			related.append(tweet)
			add_ids.add(tweet['id'])

	related = list(map(lambda t: json.dumps(t._json), related))

	if not os.path.exists(output_path):
		os.makedirs(output_path)  

	writeFile(output_path, str(tweet_id) + "_replies_others.json", related)

	return related

def isRelated(api, tweet, tweet_id):
	if tweet["id"] == tweet_id:
		return True

	if "retweeted_status" in tweet:
		result = isRelated(api, tweet["retweeted_status"], tweet_id)
		if result:
			return True

	if "quoted_status" in tweet:
		result = isRelated(api, tweet["quoted_status"], tweet_id)
		if result:
			return True

	if tweet["in_reply_to_status_id"] != None:
		reply_to = None
		try:
			reply_to = api.get_status(id=tweet["in_reply_to_status_id"], tweet_mode='extended')
		except:
			print("get_status error with id=" + tweet["in_reply_to_status_id_str"])

		if (reply_to != None):
			result = isRelated(api, reply_to._json, tweet_id)
			if result:
				return True

	return False


def writeFile(path, filename, tweets):
	if len(tweets) == 0:
		return

	o_file = open(path + "/" + filename, "w")
	o_file.write("\n".join(tweets))
