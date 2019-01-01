"""

python one.py @nytimes
python one.py @nytopinion
python one.py inputPath outputPath

"""

import sys, json, os, datetime
import tweepy
from tools import credentials as cred
from tools import rest_tools as rest
from tools import clean
from textblob import TextBlob
from tools.newstweet_tools import NewsTools

def one():

	idN = 1070755071271555072
	appN = 6
	auth = cred.getAuth(appN, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
	tool = NewsTools(api)

	# get tweet object by ID
	tweet = api.get_status(id=idN, tweet_mode='extended')

	print(str(tweet._json))
	o_file = open("this.json", "w")
	o_file.write(str(tweet._json))

def isNewsProfessional(inputPath, outputPath):

	idN = 1070755071271555072
	appN = 6
	auth = cred.getAuth(appN, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
	tool = NewsTools(api)

	userIDs = set()
	result = []

	tweets = None
	print("Processing..." + inputPath)
	with open(inputPath) as i_file:
			tweets = i_file.read().strip().split("\n")

	for t in tweets:
		t = json.loads(t)
		userID = t["user"]["id"]
		screen_name = t["user"]["screen_name"]
		if (userID not in userIDs):
			userIDs.add(userID)
			isNewsProf = tool.isNewsProfessional(t["user"]["screen_name"])
			result.append(screen_name + "\t" + str(isNewsProf))
			print(screen_name + " " + str(isNewsProf))

	o_file = open(outputPath, "w")
	o_file.write((" ".join(result)).strip())

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

def sentimentScore(text):
	# Sentiment(polarity, subjectivity)
	# The polarity score is a float within the range [-1.0, 1.0]. 
	# The subjectivity is a float within the range [0.0, 1.0] 
	t = TextBlob(text)
	return (t.sentiment.polarity, t.sentiment.subjectivity)

def getSentiment(inputPath, outputPth):
	tweets = None

	print("Processing..." + inputPath)
	with open(inputPath) as i_file:
			tweets = i_file.read().strip().split("\n")

	allSentiments = []
	totalPolarity = 0.0
	totalSubjectivity = 0.0
	for t in tweets:
		t = json.loads(t)
		(polarity, subjectivity) = sentimentScore(t["full_text"])
		allSentiments.append([str(t["id"]), str(polarity), str(subjectivity), t["full_text"]])
		totalPolarity += polarity
		totalSubjectivity += subjectivity

	allSentiments = list(map(lambda t: "\t".join(t), allSentiments))
	allSentiments_str = "\n".join(allSentiments)

	averagePolarity = totalPolarity/len(tweets)
	averageSubjectivity = totalSubjectivity/len(tweets)

	print("Saving sentiments file to..." + outputPth)

	o_file = open(outputPth, "w")
	o_file.write(allSentiments_str)

	print("Average polarity = " + str(averagePolarity))
	print("Average subjectivity = " + str(averageSubjectivity))

def main(argv):
	print("\nRunning...")
	bigFile(argv[0])
	# one()
	# clean.dedup(argv[0], argv[0], "deduped.json")
	# getSentiment(argv[0], argv[1])
	# isNewsProfessional(argv[0], argv[1])


if __name__== "__main__":
	main(sys.argv[1:])