"""

python getSource.py inputFolder outputFolder

categorize into reply/retweet/quote 

"""

import sys, datetime, os, json
from tools import general_tools as gen
from tools import credentials as cred
import tweepy

def getSource(inputFolder, outputFolder, appNumber):

	auth = cred. getAuth(appNumber, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	if not os.path.exists(outputFolder + "/NEW/"):
		os.makedirs(outputFolder + "/NEW/")

	for (dirpath, dirnames, filenames) in os.walk(inputFolder):
		for filename in filenames:
			if filename.endswith('.json'): 
				print("Currently on " + filename)
				with open(dirpath+"/"+filename) as i_file:

					iDs = set()

					f = open(outputFolder + "/NEW/" + filename+ "_source.json", "w")

					for line in i_file:
						relation = gen.getRelationNoID(line)
						toAdd = None
						t = json.loads(line)
						if relation == "retweet":
							toAdd = t["retweeted_status"]
						elif relation == "reply":
							replied = gen.getTweet(t["in_reply_to_status_id"], api)
							if replied != None:
								toAdd = json.loads(replied)
						elif relation == "quote":
							toAdd = t["quoted_status"]

						if toAdd != None:
							if toAdd["id"] not in iDs:
								f.write(line)
								iDs.add(toAdd["id"])

					f.close()


def main(argv):
	print("\nRunning...")
	# inputFolder outputFolder, appNumber
	getSource(argv[0], argv[1], int(argv[2]))

if __name__== "__main__":
	main(sys.argv[1:])