"""
Write the top n thread (full texts) into try.txt
$ python thread.py try.json maxN
"""

import sys, json, os
import tweepy
from tools import credentials as cred

input_str = ""

def printThread(path, n):

	n = int(n)

	input_str = ""
	with open(path) as i_file:
			input_str = i_file.read()

	tweets_l = input_str.split("\n")
	filename = path[:path.rindex(".")] + ".txt"
	f = None
	f = open(filename, "w")
	f.write("Extracted threads from {a} and writing into {b}\n\n---\n---\n---\n\n".format(a=path, b=filename))

	i = 2
	auth = cred.getAuth(i, "user")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	for t_str in tweets_l[:n]:
		t = json.loads(t_str)
		f.write("\n-\n")
		printTweet(api, t, f)

def printTweet(api, tweet, f, link="", level=0):

	# TODO: set up auth

	user = tweet["user"]["name"]
	full_text = tweet["full_text"]
	toPrint = "   " * level
	toPrint += link + repr(user) + ": " + repr(full_text)

	f.write("\n")
	f.write(toPrint)
	f.write("\n")

	if "retweeted_status" in tweet:
		printTweet(api, tweet["retweeted_status"], f, "Retweeting...", level=level+1)
	if "quoted_status" in tweet:
		printTweet(api, tweet["quoted_status"], f, "Quoting...", level=level+1)
	if tweet["in_reply_to_status_id"] != None:
		reply_to = None
		try:
			reply_to = api.get_status(id=tweet["in_reply_to_status_id"], tweet_mode='extended')
		except:
			print("get_status error with id=" + tweet["in_reply_to_status_id_str"])

		if (reply_to != None):
			printTweet(api, reply_to._json, f, "Replying to...", level=level+1)

def main(argv):
	print("\nRunning...")
	printThread(argv[0], argv[1])
	
if __name__== "__main__":
	main(sys.argv[1:])