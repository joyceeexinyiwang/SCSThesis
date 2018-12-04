"""

python rqr_o.py

"""

import sys, json, os, datetime
import tweepy
from tools import credentials as cred
from tools import rest_tools as rest
from tools import clean
from tools.newstweet_tools import NewsTools

def rpr():

	idN = 1069463438391459840
	appN = 3
	auth = cred.getAuth(appN, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
	tool = NewsTools(api)

	now = datetime.datetime.now()
	path = "data/@nytopinion_" + str(idN) # "data/" + str(idN) + "_" + now.strftime("%Y-%m-%d-%H-%M")

	# get tweet object by ID
	tweet = api.get_status(id=idN, tweet_mode='extended')

	print("Created at: " + tweet._json["created_at"])
	print("Retweet count = " + str(tweet._json["retweet_count"]))
	print("favorite count = " + str(tweet._json["favorite_count"]))

	scraped = []
	terms = []
	terms.append("He was all noblesse oblige")
	terms.append("nytopinion Bush")
	terms.append("nytimes Bush")
	terms.append("https://twitter.com/nytopinion/status/1069463438391459840") # full url of tweet
	terms.append("https://t.co/pDfFORy45z")
	for t in terms:
		scraped.extend(rest.rest_scrape_single(t, 1000000, api))

	scraped = list(map(lambda x: x._json, scraped))
	retweets = []
	quotes = []
	replies = []

	retweets_seen, quotes_seen, replies_seen = set(), set(), set()

	for t in scraped:
		if "retweeted_status" in t and t["retweeted_status"]["id"] == idN:
			if t["id"] not in retweets_seen:
				retweets_seen.add(t["id"])
				retweets.append(t)

		if "quoted_status" in t and t["quoted_status"]["id"] == idN:
			if t["id"] not in quotes_seen:
				quotes_seen.add(t["id"])
				quotes.append(t)

		if t["in_reply_to_status_id"] != None:
			if t["in_reply_to_status_id"] in replies_seen or t["in_reply_to_status_id"] in quotes_seen or t["in_reply_to_status_id"] in retweets_seen:
				if t["id"] not in replies_seen:
					replies_seen.add(t["id"])
					replies.append(t)

	writeFile(path, "retweets.json", retweets)
	writeFile(path, "quotes.json", quotes)
	writeFile(path, "replies.json", replies)

	readAndCategorize(path + "/@nytopinion", idN, retweets_seen, quotes_seen, replies_seen, path+"/retweets.json", path+"/quotes.json", path+"/replies.json")


def readAndCategorize(inputFolder, idN, retweets_seen, quotes_seen, replies_seen, retweets_path, quotes_path, replies_path):

	ret = open(retweets_path,'a+')
	quo = open(quotes_path,'a+')
	rep = open(replies_path,'a+')

	for (dirpath, dirnames, filenames) in os.walk(inputFolder):
		for filename in filenames:
			if filename.endswith('.json'): 
				print("Currently on " + filename)
				with open(dirpath+"/"+filename) as infile:
					for line in infile:
						# categorize
						t = json.loads(line)

						anything = False

						if "retweeted_status" in t and t["retweeted_status"]["id"] == idN:
							# if t["id"] not in retweets_seen:
							retweets_seen.add(t["id"])
							ret.write(line)
							anything = True

						if "quoted_status" in t and t["quoted_status"]["id"] == idN:
							# if t["id"] not in quotes_seen:
							quotes_seen.add(t["id"])
							quo.write(line)
							anything = True


						if t["in_reply_to_status_id"] != None:
							if t["in_reply_to_status_id"] == idN or t["in_reply_to_status_id"] in replies_seen or t["in_reply_to_status_id"] in quotes_seen or t["in_reply_to_status_id"] in retweets_seen:
								# if t["id"] not in replies_seen:
								replies_seen.add(t["id"])
								rep.write(line)
								anything = True

						# if not anything:
						# 	print(t["id"])

def writeFile(path, filename, tweets):

	if not os.path.exists(path):
		os.makedirs(path)

	ts = list(map(lambda x: json.dumps(x), tweets))

	o_file = open(path + "/" + filename, "w")
	o_file.write("\n".join(ts))

def main(argv):
	print("\nRunning...")
	rpr()
	
if __name__== "__main__":
	main(sys.argv[1:])