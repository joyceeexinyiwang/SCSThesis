"""

python one.py @nytimes
python one.py @nytopinion

"""

import sys, json, os, datetime
import tweepy
from tools import credentials as cred
from tools import rest_tools as rest
from tools import clean
from tools.newstweet_tools import NewsTools

def one():

	idN = 1069214662674264065
	appN = 6
	auth = cred.getAuth(appN, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
	tool = NewsTools(api)

	# get tweet object by ID
	tweet = api.get_status(id=idN, tweet_mode='extended')

	print(str(tweet._json))


def bigFile(term):
	appN = 4
	auth = cred.getAuth(appN, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
	now = datetime.datetime.now()
	path = "data/" + term + "_" + now.strftime("%Y-%m-%d-%H-%M")
	rest.rest_scrape([term], api, path, 100000000, file_size=100000, fileName=None, max_num_errors=5)

def writeFile(path, filename, tweets):
	if len(tweets) == 0:
		return

	if not os.path.exists(path):
		os.makedirs(path)

	ts = list(map(lambda x: json.dumps(x), tweets))

	o_file = open(path + "/" + filename, "w")
	o_file.write("\n".join(ts))

def main(argv):
	print("\nRunning...")
	# bigFile(argv[0])
	one()
		
if __name__== "__main__":
	main(sys.argv[1:])