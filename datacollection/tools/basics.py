import os, json

def dedup_and_separate(inputFolder, outputFolder, filename, keyword):

    print("## Deduplication")

    # read all tweets into lines
    allIDs = set()

    if not os.path.exists(outputFolder+"/NEW/"):
        os.makedirs(outputFolder+"/NEW/")

    maxCount = 10000

    count = 0
    fileN = 1
    f = open(outputFolder + "/NEW/" + filename + "_nonop_" + str(fileN) + ".json", "w")

    count_op = 0
    fileN_op = 1
    f_op = open(outputFolder + "/NEW/" + filename + "_op_" + str(fileN) + ".json", "w")

    for (dirpath, dirnames, filenames) in os.walk(inputFolder):
        for fname in filenames:
            if fname.endswith('.json'): 
                print("Currently on " + fname)
                with open(dirpath+"/"+fname) as i_file:

                    for line in i_file:
                        tweet = json.loads(line)
                        if tweet['id_str'] not in allIDs:
                            allIDs.add(tweet['id_str'])

                            isOp = relatedToOpinion(tweet, keyword)

                            if isOp:
                                f_op.write(line)
                                count_op += 1
                                if count_op >= maxCount:
                                    count_op = 0
                                    f_op.close()
                                    fileN_op += 1
                                    print("New file")
                                    f_op = open(outputFolder + "/NEW/" + filename + "_op_" + str(fileN_op) + ".json", "w")
                            else:
                                f.write(line)
                                count += 1
                                if count >= maxCount:
                                    count = 0
                                    f.close()
                                    fileN += 1
                                    print("New file")
                                    f = open(outputFolder + "/NEW/" + filename + "_nonop_" + str(fileN) + ".json", "w")

    f.close()
    f_op.close()
    print("..." + str(len(allIDs)) + " tweets so far")


def relatedToOpinion(t, keyword):
    isOp = keyword in t["full_text"]
    if isOp:
        return True

    if "retweeted_status" in t:
        retweet = t["retweeted_status"]
        if keyword in retweet["full_text"]: 
            isOp = True

        if "retweeted_status" in retweet:
            retweet_2 = retweet["retweeted_status"]
            if keyword in retweet_2["full_text"]: 
                isOp = True

        if "quoted_status" in retweet:
            quote_2 = retweet["quoted_status"]
            if keyword in quote_2["full_text"]: 
                isOp = True

    if "quoted_status" in t:
        quote = t["quoted_status"]
        if keyword in quote["full_text"]: 
            isOp = True

        if "retweeted_status" in quote:
            retweet_2 = quote["retweeted_status"]
            if keyword in retweet_2["full_text"]: 
                isOp = True

        if "quoted_status" in quote:
            quote_2 = quote["quoted_status"]
            if keyword in quote_2["full_text"]: 
                isOp = True

    return isOp


def dedup(inputFolder, outputFolder, filename):

    print("## Deduplication")

    # read all tweets into lines
    allIDs = set()

    if not os.path.exists(outputFolder+"/NEW/"):
        os.makedirs(outputFolder+"/NEW/")

    count = 0
    maxCount = 10000
    fileN = 1
    f = open(outputFolder + "/NEW/" + filename + "_" + str(fileN) + ".json", "w")

    for (dirpath, dirnames, filenames) in os.walk(inputFolder):
        for filename in filenames:
            if filename.endswith('.json'): 
                print("Currently on " + filename, end="")
                with open(dirpath+"/"+filename) as i_file:

                    for line in i_file:
                        tweet = json.loads(line)
                        if tweet['id_str'] not in allIDs:
                            f.write(line)
                            allIDs.add(tweet['id_str'])

                            count += 1
                            if count >= maxCount:
                                count = 0
                                f.close()
                                fileN += 1
                                print("New file")
                                f = open(outputFolder + "/" + filename + "_" + str(fileN) + ".json", "w")

                    f.close()

                print("..." + str(len(allIDs)) + " tweets so far")


def dedup_2(inputFolder, outputFolder, outputFile):
    ids = set()

    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)
        
    for (dirpath, dirnames, filenames) in os.walk(inputFolder):
        for filename in filenames:
            if filename.endswith('.json'): 
                print("Currently on " + filename)
                with open(dirpath+"/"+filename) as f:
                    fd = open(outputFolder+"/" + outputFile + "_"+filename+".csv", "w")
                    for line in f:
                        i = json.loads(line)["id"]
                        if i not in ids:
                            fd.write(line)
                            ids.add(i)
                    fd.close()

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