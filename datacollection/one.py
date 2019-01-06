"""

python one.py keyword outputFolder appNumber

"""

import sys, datetime
import tweepy
from tools import credentials as cred
from tools import rest_tools as rest

def bigFile(term, outputFolder, appNumber):
	appN = appNumber
	auth = cred.getAuth(appN, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
	now = datetime.datetime.now()
	path = outputFolder + "/" + term + "_" + now.strftime("%Y-%m-%d-%H-%M")
	rest.rest_scrape([term], api, path, 100000000, file_size=10000, fileName=None, max_num_errors=5)

def main(argv):
	print("\nRunning...")
	# keyword outputFolder appNumber
	bigFile(argv[0], argv[1], int(argv[2]))

if __name__== "__main__":
	main(sys.argv[1:])