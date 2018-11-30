"""
Write the top n thread (full texts) into try.txt
$ python thread.py xxx.json 0 100 1
"""

import sys, json, os
import tweepy
from tools import credentials as cred
from tools.newstweet_tools import NewsTools

def printThread(path, startN, endN, appN):

	input_str = ""
	with open(path) as i_file:
		input_str = i_file.read()

	tweets_l = input_str.split("\n")
	folderName = path[:path.rindex(".")] + "_thread"
	if not os.path.exists(folderName):
		os.makedirs(folderName)

	count = 0
	size = 10
	fileCount = 0

	filename = "thread_" + str(count) + "_" + str(count + size) + ".txt"
	f = open(folderName + "/" + filename, "w")
	f.write("Extracted threads from {a} and writing into {b}\n\n---\n---\n---\n\n".format(a=folderName, b=filename))

	i = appN
	auth = cred.getAuth(i, "user")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	tool = NewsTools(api)

	agents = {}

	for t_str in tweets_l[startN:endN]:

		print("woop")
		t = json.loads(t_str)
		f.write("\n-\n")
		a = printTweet(tool, t, f, agents)
		agents.update(a)

		count += 1
		if count >= size:
			count = 0
			fileCount += 1
			filename = "thread_" + str(startN + fileCount * size) + "_" + str(startN + fileCount * size + size) + ".txt"
			f = open(folderName + "/" + filename, "w")
			f.write("Extracted threads from {a} and writing into {b}\n\n---\n---\n---\n\n".format(a=folderName, b=filename))


	filename_a = "thread_agents.txt"
	f = None
	f = open(folderName + "/" + filename_a, "w")
	f.write(json.dumps(agents))

def printTweet(tool, tweet, f, agents, link="", level=0):

	# TODO: set up auth



	# if (tweet["user"]["screen_name"] in agents):
	# 	user_profile = agents[tweet["user"]["screen_name"]]
	# else:
	# 	user_profile = tool.profileAgent(tweet)
	# 	agents[user_profile["handle"]] = user_profile

	user = tweet["user"]["screen_name"]
		# user_profile["handle"] \
		# + " [" + user_profile["profession"] + ", " \
		# + user_profile["influence"] + " influence, " \
		# + user_profile["activeness"] + "]"

	full_text = tweet["full_text"]

	opinionScore = tool.opinionScore(tweet)

	toPrint = "   " * level
	toPrint += link
	toPrint += user + ": "
	toPrint += "\n" + "   " * level
	toPrint += "[OPINION: " + str(opinionScore) + "/1.0]" + repr(full_text)

	f.write("\n")
	f.write(toPrint)
	f.write("\n")

	if "retweeted_status" in tweet:
		a = printTweet(tool, tweet["retweeted_status"], f,  agents, "Retweeting...", level=level+1)
		agents.update(a)
	if "quoted_status" in tweet:
		a = printTweet(tool, tweet["quoted_status"], f,  agents, "Quoting...", level=level+1)
		agents.update(a)
	if tweet["in_reply_to_status_id"] != None:
		reply_to = None
		try:
			reply_to = tool.api.get_status(id=tweet["in_reply_to_status_id"], tweet_mode='extended')
		except:
			print("get_status error with id=" + tweet["in_reply_to_status_id_str"])

		if (reply_to != None):
			a = printTweet(tool, reply_to._json, f,  agents, "Replying to...", level=level+1)
			agents.update(a)

	return agents

def main(argv):
	print("\nRunning...")
	printThread(argv[0], int(argv[1]), int(argv[2]), int(argv[3]))
	
if __name__== "__main__":
	main(sys.argv[1:])