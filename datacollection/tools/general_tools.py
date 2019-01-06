import datetime, time, sys, json
import tweepy
from tools import credentials

def getTweet(tweet_id, api):
	tweet = api.get_status(id=tweet_id, tweet_mode='extended')
	return json.dumps(tweet._json)

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