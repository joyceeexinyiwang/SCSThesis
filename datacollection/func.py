"""

python func.py tweetID appNumber

"""

import sys
import tweepy
from tools import general_tools as gen
from tools import credentials

def main(argv):
	print("\nRunning...")
	
	idN = int(argv[0])
	i = int(argv[1])
	auth = credentials. getAuth(i, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	tweet = gen.getTweet(idN, api)

	print(tweet)
	
if __name__== "__main__":
	main(sys.argv[1:])