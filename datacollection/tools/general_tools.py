import datetime, time, sys, json
import tweepy
from tools import credentials

def getTweet(tweet_id, api):
	try:
		tweet = api.get_status(id=tweet_id, tweet_mode='extended')
		return json.dumps(tweet._json)
	except:
		print("No status found with that ID: " + str(tweet_id))

def getFriends(user_id, api):
	friends = []
	for page in tweepy.Cursor(api.friends_ids, id=user_id, tweet_mode='extended').pages():
	    friends.extend(page)

	return friends

def getFollowers(user_id, api):
	followers = []
	for page in tweepy.Cursor(api.followers_ids, id=user_id, tweet_mode='extended').pages():
	    followers.extend(page)

	return followers

def getTimeline(user_id, api):	
	tweets = []
	for page in tweepy.Cursor(api.user_timeline, id=user_id, tweet_mode='extended', count=20).pages():
	    tweets.extend(page)

	tweet_str_list = []
	for t in tweets:
		tweet_str_list.append(t._json)

	return tweet_str_list

def getRelation(t_str, idN):
	t = json.loads(t_str)
	relation = None

	if "retweeted_status" in t and t["retweeted_status"]["id"] == idN:
		relation = "retweet"

	if "quoted_status" in t and t["quoted_status"]["id"] == idN:
		relation = "quote"

	if t["in_reply_to_status_id"] != None:
		if t["in_reply_to_status_id"] == idN:
			relation = "reply"

	return relation

def getRelationNoID(t_str):
	try:
		t = json.loads(t_str)
	except:
		print(t_str)
		return
	relation = None

	if "retweeted_status" in t:
		relation = "retweet"

	if "is_quote_status" in t and t["is_quote_status"] == True:
		relation = "quote"

	if t["in_reply_to_status_id"] != None:
		relation = "reply"

	return relation
