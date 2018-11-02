"""
code snippets:
http://docs.tweepy.org/en/v3.5.0/code_snippet.html

API reference:
http://docs.tweepy.org/en/v3.5.0/api.html


$ python user.py 

"""

import datetime, time, sys, json
import tweepy
from tools import credentials

def getFriends(user_id):
	i = 0
	auth = credentials.getAuth(i, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	friends = []
	for page in tweepy.Cursor(api.friends_ids, id=user_id, tweet_mode='extended').pages():
	    friends.extend(page)

	return friends

def getFollowers(user_id):
	i = 0
	auth = credentials. getAuth(i, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	followers = []
	for page in tweepy.Cursor(api.followers_ids, id=user_id, tweet_mode='extended').pages():
	    followers.extend(page)

	return followers

def getTimeline(user_id):	

	i = 0
	auth = credentials. getAuth(i, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	tweets = []
	for page in tweepy.Cursor(api.user_timeline, id=user_id, tweet_mode='extended', count=20).pages():
	    tweets.extend(page)

	tweet_str_list = []
	for t in tweets:
		tweet_str_list.append(json.dumps(t._json))

	writeFile(user_id, tweet_str_list)

	# for t in tweets:
	# 	try:
	# 		print(t.retweeted_status.full_text)
	# 	except:
	# 		print(t.full_text)

def getSourceID(user_id):
	i = 0
	auth = credentials.getAuth(i, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
	user = api.get_user(id="_vaguely_")
	return user.id

def writeEdgeList(filename, user_id, content):
    o_file = open(filename + "_" + str(user_id) + ".csv", "w")

    edgeList = []
    for f in content:
    	edgeList.append(str(user_id) + "," + str(f))

    o_file.write("\n".join(edgeList))


def writeFile(user_id, tweets):
	o_file = open(str(user_id) + ".json", "w")
	o_file.write("\n".join(tweets))

# def main(argv):
#   print("Running")

#   user_id = "_vaguely_"
#   source_id = getSourceID(user_id)
#   friends = getFriends(user_id)
#   followers = getFollowers(user_id)

#   #and dedup

#   writeEdgeList("./data/friends", source_id, friends)
#   writeEdgeList("./data/followers", source_id, followers)

#   getTimeline("km")
  
# if __name__== "__main__":
#   main(sys.argv)



# # Iterate through all of the authenticated user's friends
# for friend in tweepy.Cursor(api.friends).items():
#     # Process the friend here
#     process_friend(friend)

# # Iterate through the first 200 statuses in the friends timeline
# for status in tweepy.Cursor(api.friends_timeline).items(200):
#     # Process the status here
#     process_status(status)