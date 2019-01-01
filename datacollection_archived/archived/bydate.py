"""
INPUT: directory path, json file of tweets
OUTPUT: json files, each containing tweets on a certain date

$ python bydate.py path filename

"""


import sys, json

def run(path, filename):

	# read all tweets into lines

	allTweets = {}

	with open(path + "/" + filename) as i_file:
         for line in i_file:
         	tweet = json.loads(line)
         	created_at = tweet["created_at"]
         	#"created_at": "Tue Oct 30 17:11:39 +0000 2018"
         	date = "_".join((created_at.split(" "))[1:3])
         	if date not in allTweets:
         		allTweets[date] = []
         	allTweets[date].append(line.strip())

	#write allTweets in file
	for date in allTweets:
		tweets = allTweets[date]
		writeFile(date, path, tweets)

def writeFile(date, path, tweets):
    o_file = open(path + "/" + date + ".json", "w")
    o_file.write("\n".join(tweets))

def main(argv):
  print("Running")
  run(argv[0], argv[1])
  
if __name__== "__main__":
  main(sys.argv[1:])
