"""

dedup and consolidate

$ python dedup.py folder

*make sure deduped.csv is NOT in the folder already!

"""

import json, sys, os

def run(path):

    # read all tweets into lines
    allIDs = set()
    allTweets = []

    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if filename.endswith('.json'): 
                print("Processing: " + filename, end="")
                with open(dirpath+"/"+filename) as i_file:
                    for line in i_file:
                        tweet = json.loads(line)
                        if tweet['id'] not in allIDs:
                            allTweets.append(line.strip())
                            allIDs.add(tweet['id'])
                print("..." + str(len(allTweets)) + " tweets so far")

    #write allTweets in file
    writeFile(path, allTweets)

def writeFile(path, tweets):
    o_file = open(path + "/deduped.json", "w")
    o_file.write("\n".join(tweets))

def main(argv):
  print("Running")
  run(argv[0])

if __name__== "__main__":
  main(sys.argv[1:])
