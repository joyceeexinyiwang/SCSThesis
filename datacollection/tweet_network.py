"""

retweet: query by keywords of original tweets and filter
quote: query by url and filter
reply: query by news agency handle and filter

python tweet_network.py keywords.tsv outputFolder appNumber

"""

import sys, json, os, datetime
import tweepy
from tools import credentials as cred
from tools import rest_tools as rest
from tools import basics


def network(idN, excerpts, links, path, appN):

	auth = cred.getAuth(appN, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	now = datetime.datetime.now()
	path = path + "_" + now.strftime("%Y-%m-%d-%H-%M")

	# get tweet object by ID
	tweet = api.get_status(id=idN, tweet_mode='extended')

	print("Created at: " + tweet._json["created_at"])
	print("Retweet count = " + str(tweet._json["retweet_count"]))
	print("Favorite count = " + str(tweet._json["favorite_count"]))

	scraped = []
	terms = []
	terms.extend(excerpts)
	terms.extend(links)
	for t in terms:
		scraped.extend(rest.rest_scrape_single(t, 1000000, api))

	scraped = list(map(lambda x: x._json, scraped))
	basics.writeFile(path, "all.json", list(map(lambda x: json.dumps(x), scraped)))

	retweets = []
	quotes = []
	replies = []

	retweets_seen, quotes_seen, replies_seen = set(), set(), set()

	for t in scraped:
		if "retweeted_status" in t and t["retweeted_status"]["id"] == idN:
			if t["id"] not in retweets_seen:
				retweets_seen.add(t["id"])
				retweets.append(t)

		if "quoted_status" in t and t["quoted_status"]["id"] == idN:
			if t["id"] not in quotes_seen:
				quotes_seen.add(t["id"])
				quotes.append(t)

		if t["in_reply_to_status_id"] != None:
			if t["in_reply_to_status_id"] in replies_seen or t["in_reply_to_status_id"] in quotes_seen or t["in_reply_to_status_id"] in retweets_seen:
				if t["id"] not in replies_seen:
					replies_seen.add(t["id"])
					replies.append(t)

	ids = list(map(lambda x: x["id"], retweets))
	ids.extend(list(map(lambda x: x["id"], quotes)))
	ids.extend(list(map(lambda x: x["id"], replies)))
	ids = list(map(lambda x: str(x), ids))
	ids.append(str(idN))

	basics.writeFile(path, "ids.csv", [",".join(ids)]);
	basics.writeFile(path, "retweets.json", list(map(lambda x: json.dumps(x), retweets)))
	basics.writeFile(path, "quotes.json", list(map(lambda x: json.dumps(x), quotes)))
	basics.writeFile(path, "replies.json", list(map(lambda x: json.dumps(x), replies)))

	# readAndCategorize(path, idN, retweets_seen, quotes_seen, replies_seen, path+"/retweets.json", path+"/quotes.json", path+"/replies.json")


def readAndCategorize(inputFolder, idN, retweets_seen, quotes_seen, replies_seen, retweets_path, quotes_path, replies_path):

	ret = open(retweets_path,'a+')
	quo = open(quotes_path,'a+')
	rep = open(replies_path,'a+')

	for (dirpath, dirnames, filenames) in os.walk(inputFolder):
		for filename in filenames:
			if filename.endswith('.json'): 
				print("Currently on " + filename)
				with open(dirpath+"/"+filename) as infile:
					for line in infile:
						# categorize
						t = json.loads(line)

						anything = False

						if "retweeted_status" in t and t["retweeted_status"]["id"] == idN:
							# if t["id"] not in retweets_seen:
							retweets_seen.add(t["id"])
							ret.write(line)
							anything = True

						if "quoted_status" in t and t["quoted_status"]["id"] == idN:
							# if t["id"] not in quotes_seen:
							quotes_seen.add(t["id"])
							quo.write(line)
							anything = True


						if t["in_reply_to_status_id"] != None:
							if t["in_reply_to_status_id"] == idN or t["in_reply_to_status_id"] in replies_seen or t["in_reply_to_status_id"] in quotes_seen or t["in_reply_to_status_id"] in retweets_seen:
								# if t["id"] not in replies_seen:
								replies_seen.add(t["id"])
								rep.write(line)
								anything = True

						# if not anything:
						# 	print(t["id"])

def main(argv):
	print("\nRunning...")

	# keywords.tsv outputFolder appNumber

	tsv = argv[0]
	outputFolder = argv[1]
	appN = int(argv[2])

	with open(tsv) as i_file:
		qlist = i_file.read()
	queries = qlist.split("\n")
	tweetID = int(queries[0])
	excerpts = queries[1].split("\t")
	links = queries[2].split("\t")

	network(tweetID, excerpts, links, outputFolder, appN)
	
if __name__== "__main__":
	main(sys.argv[1:])