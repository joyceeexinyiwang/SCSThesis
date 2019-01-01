"""

python filter.py data/try sample.json PittsburghPG 100000000 0

"""

import datetime, sys, os, json
import tweepy
from tools import credentials as cred
from tools import rest_tools as rest
from tools import clean
from tools import newstweet_tools as news


def filter(inputFolder, inputFile, handle, maxTweets, appN):
	inTweets = ""
	with open(inputFolder + "/" + inputFile) as i_file:
		inTweets = i_file.read()
	tweets = inTweets.split("\n")

	auth = cred.getAuth(appN, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	relevantTweets = []
	irrelevantTweets = []
	for tweet in tweets:
		if news.isRelatedToAgency(api, json.loads(tweet), handle):
			relevantTweets.append(tweet)
		else:
			irrelevantTweets.append(tweet)

	outpath = inputFolder + "/result"

	if not os.path.exists(outpath):
		os.makedirs(outpath)  

	writeFile(outpath, "relevant.json", relevantTweets)
	writeFile(outpath, "irrelevant.json", irrelevantTweets)
	clean.dedup(inputFolder, outpath)

def writeFile(path, filename, tweets):
	if len(tweets) == 0:
		return

	o_file = open(path + "/" + filename, "w")
	o_file.write("\n".join(tweets))

def main(argv):
	filter(argv[0], argv[1], argv[2], int(argv[3]), int(argv[4]))
  
if __name__== "__main__":
	main(sys.argv[1:])



# - query by url and filter by quote status to get **quotes**
# - get all tweets with @newsorg and filter by reply status to get **replies**
# - query by a section of the tweet and then filter by retweet status to get **retweets**