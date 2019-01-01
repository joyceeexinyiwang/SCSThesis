"""

"""

import json, sys, os
import tweepy
from tools import newstweet_tools as news
from tools import credentials as cred

def dedup(inputFolder, outputFolder, outputFile):

    print("## Deduplication")

    # read all tweets into lines
    allIDs = set()
    allTweets = []

    for (dirpath, dirnames, filenames) in os.walk(inputFolder):
        for filename in filenames:
            if filename.endswith('.json'): 
                print("Currently on " + filename, end="")
                with open(dirpath+"/"+filename) as i_file:
                    for line in i_file:
                        tweet = json.loads(line)
                        if tweet['id'] not in allIDs:
                            allTweets.append(line.strip())
                            allIDs.add(tweet['id'])
                print("..." + str(len(allTweets)) + " tweets so far")

    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)  

    writeFile(outputFolder, outputFile, allTweets)

    return allTweets

def dedupFile(inputFile, outputFolder, outputFile):
    allIDs = set()
    allTweets = []
    with open(inputFile) as i_file:
        for line in i_file:
            tweet = json.loads(line)
            if tweet['id'] not in allIDs:
                allTweets.append(line.strip())
                allIDs.add(tweet['id'])
                
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)  

    writeFile(outputFolder, outputFile, allTweets)

    return allTweets

def separateByDate(allTweets, outputFolder):

    print("## Separate tweets by date")

    allTweets_dict = {}

    for line in allTweets:
        tweet = json.loads(line)
        created_at = tweet["created_at"]
        #"created_at": "Tue Oct 30 17:11:39 +0000 2018"
        date = "_".join((created_at.split(" "))[1:3])
        if date not in allTweets_dict:
            allTweets_dict[date] = []
        allTweets_dict[date].append(line.strip())

    for date in allTweets_dict:
        tweets = allTweets_dict[date]
        writeFile(outputFolder, date + ".json", tweets)

    return allTweets_dict

def filter(tool, inputFolder, inputFile, outputFolder, handle, maxTweets, appN):

    print("## Filtering by relevance to @" + handle)

    inTweets = ""
    with open(inputFolder + "/" + inputFile) as i_file:
        inTweets = i_file.read()
    tweets = inTweets.split("\n")

    auth = cred.getAuth(appN, "app")
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    relevantTweets = []
    irrelevantTweets = []

    for tweet in tweets:
        print(".", end="")
        (result, accum) = tool.isRelatedToAgency(json.loads(tweet), handle)
        if result:
            relevantTweets.append(tweet)
            relevantTweets.extend(accum)
        else:
            irrelevantTweets.append(tweet)
            relevantTweets.extend(accum)

    writeFile(inputFolder, "relevant.json", relevantTweets)
    writeFile(inputFolder, "irrelevant.json", irrelevantTweets)

    return (relevantTweets, irrelevantTweets)

def writeFile(path, filename, tweets):
    if not os.path.exists(path):
        os.makedirs(path)

    o_file = open(path + "/" + filename, "w")
    o_file.write("\n".join(tweets))



# def clean(input_folder, output_path):

#     print("## Cleaning {}".format(input_folder), end="")
#     print (" and writing cleaned files into {}".format(output_path))

#     # DEDUPLICATION
#     allTweets = dedup(input_folder, output_path)

#     # SEPARATE BY DATE
#     allTweets_dict = separateByDate(allTweets)


def main(argv):
  print("Running")
  clean(argv[0], argv[1])
  
if __name__== "__main__":
  main(sys.argv[1:])