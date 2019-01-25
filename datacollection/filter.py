"""

python filter.py newsagency inputFolder outputFolder appNumber

"""

import sys, datetime, os, json
from tools import general_tools as gen
from tools import credentials as cred
import tweepy

def filter(newsagency, inputFolder, outputFolder, appNumber):

	auth = cred. getAuth(appNumber, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	if not os.path.exists(outputFolder):
		os.makedirs(outputFolder)

	count = 0
	maxCount = 10000
	fileN = 1
	f = open(outputFolder + "/" + newsagency + "_" + str(fileN) + ".json", "w")

	# 0 -> opinion, 1 -> nonopinion
	counts = [0, 0]
	maxCount = 10000
	fileNs = [1, 1]
	fs = [None] * 2
	if not os.path.exists(outputFolder + "/NEW/"):
		os.makedirs(outputFolder + "/NEW/")
	fs[0] = open(outputFolder + "/NEW/" + newsagency + "_op_" + str(fileNs[0]) + ".json", "w")
	fs[1] = open(outputFolder + "/NEW/" + newsagency + "_nonop_" + str(fileNs[1]) + ".json", "w")

	keyword = "opinion"

	# read all tweets in the directory
	for (dirpath, dirnames, filenames) in os.walk(inputFolder):
		for filename in filenames:
			if filename.endswith('.json'): 
				with open(dirpath+"/"+filename) as infile:
					print("Currently on " + filename)
					for line in infile:
						toAdd = None
						origin = None
						t = json.loads(line)

						# check if this tweet can be traced to the news agency

						if "retweeted_status" in t:
							if t["retweeted_status"]["user"]["screen_name"].lower() == newsagency.lower():
								toAdd = line
								origin = t["retweeted_status"]

						if "quoted_status" in t:
							if t["quoted_status"]["user"]["screen_name"].lower() == newsagency.lower():
								toAdd = line
								origin = t["quoted_status"]

						if t["in_reply_to_screen_name"] != None and t["in_reply_to_screen_name"].lower() == newsagency.lower(): 
							toAdd = line
							replied = gen.getTweet(t["in_reply_to_status_id"], api)
							if replied != None:
								origin = json.loads(replied)
							else:
								print("! Reply with user id but no reply status id::: id=" + str(t["id"]) + "; in_reply_to_status_id=" + str(t["in_reply_to_status_id"]))

						if toAdd != None:
							f.write(toAdd)
							count += 1
							if count >= maxCount:
								count = 0
								f.close()
								fileN += 1
								print("New file")
								f = open(outputFolder + "/" + newsagency + "_" + str(fileN) + ".json", "w")
	
							# separate by #opinion or opinion tags in the original tweet
							# and get stats based on that

							if origin != None:
								full_text = origin["full_text"]
								if "opinion" in full_text.lower():
									fs[0].write(line)
									counts[0] += 1

									if counts[0] >= maxCount:
										counts[0] = 0
										fs[0].close()
										fileNs[0] += 1
										print("New file")
										fs[0] = open(outputFolder + "/NEW/" + newsagency + "_op_" + str(fileNs[0]) + ".json", "w")

								else:
									fs[1].write(line)
									counts[1] += 1

									if counts[1] >= maxCount:
										counts[1] = 0
										fs[1].close()
										fileNs[1] += 1
										print("New file")
										fs[1] = open(outputFolder + "/NEW/" + newsagency + "_nonop_" + str(fileNs[1]) + ".json", "w")

	f.close()
	fs[0].close()
	fs[1].close()

def main(argv):
	print("\nRunning...")
	# keyword outputFolder appNumber
	filter(argv[0], argv[1], argv[2], int(argv[3]))

if __name__== "__main__":
	main(sys.argv[1:])