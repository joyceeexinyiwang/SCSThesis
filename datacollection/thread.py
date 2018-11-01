"""

$ python thread.py try.json

"""

import sys, json, os

input_str = ""

def printThread(path):

	input_str = ""
	with open(path) as i_file:
			input_str = i_file.read()

	tweets = json.loads(input_str)
	tweets_l = tweets.split("\n")

	filename = path[:path.rindex(".")] + ".txt"
	f = None
	f = open(filename, "w")
	f.write("Extracted threads from {a} and writing into {b}\n\n---\n---\n---\n\n".format(a=path, b=filename))

	for t in tweets_l:
		printTweet(t, f)

def printTweet(tweet, f, link="", level=0):
	user = tweet["user"]["name"]
	full_text = tweet["full_text"]
	toPrint = "   " * level
	toPrint += repr(user) + " " + link + ": " + repr(full_text)

	print(toPrint)
	f.write("\n")
	f.write(toPrint)
	f.write("\n")

	if "retweeted_status" in tweet:
		printTweet(tweet["retweeted_status"], f, "retweeted", level+1)
	if "quoted_status" in tweet:
		printTweet(tweet["quoted_status"], f, "quoted", level+1)

def main(argv):
	print("\nRunning...")
	printThread(argv[0])
	
if __name__== "__main__":
	main(sys.argv[1:])