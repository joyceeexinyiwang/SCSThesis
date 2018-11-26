"""
Write the top n thread (full texts) into try.txt
$ python thread.py try.json 100 2
"""

import sys, json, os
import tweepy
from tools import credentials as cred
from tools import newstweet_tools as news

input_str = ""

def printThread(path, n, appN):

	n = int(n)

	input_str = ""
	with open(path) as i_file:
			input_str = i_file.read()

	tweets_l = input_str.split("\n")
	filename = path[:path.rindex(".")] + "_thread.txt"
	f = None
	f = open(filename, "w")
	f.write("Extracted threads from {a} and writing into {b}\n\n---\n---\n---\n\n".format(a=path, b=filename))

	i = appN
	auth = cred.getAuth(i, "user")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	agents = {}

	for t_str in tweets_l[:n]:
		print("woop")
		t = json.loads(t_str)
		f.write("\n-\n")
		a = printTweet(api, t, f, agents)
		agents.update(a)


	filename_a = path[:path.rindex(".")] + "_thread_agents.txt"
	f = None
	f = open(filename_a, "w")
	f.write(json.dumps(agent))



def printTweet(api, tweet, f, agents, link="", level=0):

	# TODO: set up auth

	if (tweet["user"]["screen_name"] in agents):
		user_profile = agents[tweet["user"]["screen_name"]]
	else:
		user_profile = news.profileAgent(api, tweet)
		agents[user_profile["handle"]] = user_profile

	user = user_profile["handle"] + ": " \
		+ user_profile["profession"] + ", " \
		+ user_profile["influence"] + " influence, " \
		+ user_profile["activeness"]

	full_text = tweet["full_text"]
	toPrint = "   " * level
	toPrint += link
	toPrint += user + ": "
	toPrint += "\n" + "   " * level
	toPrint += repr(full_text)

	f.write("\n")
	f.write(toPrint)
	f.write("\n")

	if "retweeted_status" in tweet:
		a = printTweet(api, tweet["retweeted_status"], f,  agents, "Retweeting...", level=level+1)
		agents.update(a)
	if "quoted_status" in tweet:
		a = printTweet(api, tweet["quoted_status"], f,  agents, "Quoting...", level=level+1)
		agents.update(a)
	if tweet["in_reply_to_status_id"] != None:
		reply_to = None
		try:
			reply_to = api.get_status(id=tweet["in_reply_to_status_id"], tweet_mode='extended')
		except:
			print("get_status error with id=" + tweet["in_reply_to_status_id_str"])

		if (reply_to != None):
			a = printTweet(api, reply_to._json, f,  agents, "Replying to...", level=level+1)
			agents.update(a)

	return agents

def main(argv):
	print("\nRunning...")
	printThread(argv[0], argv[1], int(argv[2]))
	
if __name__== "__main__":
	main(sys.argv[1:])