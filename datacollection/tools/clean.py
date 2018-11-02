"""

depulication and separate twitters by date, sequentially

$ python clean.py input_folder output_path

"""

import json, sys, os

def clean(input_folder, output_path):

    print("## Cleaning {}".format(input_folder))

    # DEDUPLICATION

    # read all tweets into lines
    allIDs = set()
    allTweets = []

    for (dirpath, dirnames, filenames) in os.walk(input_folder):
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


    # SEPARATE BY DATE

    allTweets_dict = {}

    for line in allTweets:
        tweet = json.loads(line)
        created_at = tweet["created_at"]
        #"created_at": "Tue Oct 30 17:11:39 +0000 2018"
        date = "_".join((created_at.split(" "))[1:3])
        if date not in allTweets_dict:
            allTweets_dict[date] = []
        allTweets_dict[date].append(line.strip())


    # WRITE INTO FILES

    print ("## Writing cleaned files into {}".format(output_path))

    if not os.path.exists(output_path):
        os.makedirs(output_path)  

    writeFile(output_path, "deduped.json", allTweets)

    for date in allTweets_dict:
        tweets = allTweets_dict[date]
        writeFile(output_path, date + ".json", tweets)


def writeFile(path, filename, tweets):
    o_file = open(path + "/" + filename, "w")
    o_file.write("\n".join(tweets))

def main(argv):
  print("Running")
  clean(argv[0], argv[1])
  
if __name__== "__main__":
  main(sys.argv[1:])