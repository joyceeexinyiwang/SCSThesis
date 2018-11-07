"""

python newstory.py data/try sample.json 100000000 0 f PittsburghPG

"""

import datetime, sys, json
import tweepy
from tools import credentials as cred
from tools import rest_tools as rest
from tools import clean
from tools import newstweet_tools as news

def scrape_from_tweets(inputFolder, inputFile, maxTweets, appN):   

	#Create Query list
	inTweets = ""
	with open(inputFolder + "/" + inputFile) as i_file:
		inTweets = i_file.read()
	tweets = inTweets.split("\n")

	auth = cred.getAuth(appN, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	outpath = inputFolder + "/result"

	for tweet in tweets:
		jt = json.loads(tweet)
		tweet_id = jt["id"]
		account_handle = jt["user"]["screen_name"]

		op = outpath

		tweet_segment = " ".join((jt["full_text"].split(" "))[2:min(10, len(jt["full_text"].split(" "))-2)])

		if (tweet_segment != ""):
			retweets = news.getRetweets(api, op, maxTweets, tweet_segment, tweet_id)

		try:
			tweet_url = jt["entities"]["urls"]["url"]
			quotes = news.getQuotes(api, op, maxTweets, tweet_url, tweet_id)
		except:
			print("\t\tCan't find tweet url for id=" + str(tweet_id))
		
		replies_and_others = news.getRepliesAndOthers(api, op, maxTweets, account_handle, tweet_id)

	clean.clean(outpath, outpath)

def scrape_from_id(inputFolder, inputFile, maxTweets, appN):   

	#Create Query list
	ids = ""
	with open(inputFolder + "/" + inputFile) as i_file:
		inTweets = i_file.read()
	ids = ids.split("\n")

	auth = cred.getAuth(appN, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	outpath = inputFolder + "/result"

	for curID in ids:

		tweet = None
		try:
			tweet = api.get_status(id=int(curID), tweet_mode='extended')
		except:
			print("get_status error with id=" + curID)

		jt = tweet._json
		tweet_id = jt["id"]
		account_handle = jt["user"]["screen_name"]
		tweet_segment = " ".join((jt["full_text"].split(" "))[2:])

		op = outpath

		retweets = news.getRetweets(api, op, maxTweets, tweet_segment, tweet_id)

		try:
			tweet_url = jt["entities"]["urls"]["url"]
			quotes = news.getQuotes(api, op, maxTweets, tweet_url, tweet_id)
		except:
			print("Can't find tweet url for id=" + str(tweet_id))
		
		replies_and_others = news.getRepliesAndOthers(api, op, maxTweets, account_handle, tweet_id)

	clean.clean(outpath, outpath)


def filter(inputFolder, inputFile, maxTweets, appN):
	inTweets = ""
	with open(inputFolder + "/" + inputFile) as i_file:
		inTweets = i_file.read()
	tweets = inTweets.split("\n")

	auth = cred.getAuth(appN, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	outpath = inputFolder + "/result"

	for tweet in tweets:

def main(argv):
	print("")
	# inputFolder, inputFile, maxTweet, app number, whether starting from tweets, or from tweet ID's
	if argv[4] == "t":
		scrape_from_tweets(argv[0], argv[1], int(argv[2])
			, int(argv[3]))
	elif argv[4] == "i":
		scrape_from_id(argv[0], argv[1], int(argv[2]), int(argv[3]))
	elif argv[4] == "f":
		filter(argv[0], argv[1], int(argv[2]), int(argv[3]), agrv[])
	else:
		print("Illegal 3rd argument: 't', 'i', or 'f'.")
  
if __name__== "__main__":
	main(sys.argv[1:])



# - query by url and filter by quote status to get **quotes**
# - get all tweets with @newsorg and filter by reply status to get **replies**
# - query by a section of the tweet and then filter by retweet status to get **retweets**