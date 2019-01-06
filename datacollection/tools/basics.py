import os, json

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

def writeFile(path, filename, tweets):
    if not os.path.exists(path):
        os.makedirs(path)

    o_file = open(path + "/" + filename, "w")
    o_file.write("\n".join(tweets))