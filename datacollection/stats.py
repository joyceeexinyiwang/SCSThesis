"""

python stats.py directory file

"""

import sys, datetime, os, json, csv

def lengths(directory, file):

    if not os.path.exists(directory + "/NEW/"):
        os.makedirs(directory + "/NEW/")

    # total lengths of tweet
    total_length = 0

    # total number of tweets
    total_N = 0

    # FLAG: tons of hashtag
    flag_hashtags_N = 0

    # FLAG: You statements
    flag_you_N = 0

    # share words with original tweets 
    # FLAG: I statements  
    # FLAG: no I or you
    # stratification tweet length

    # each row is a tweet
    # columns: full_text length, flag_hashtags, flag_you, # of shared words with original tweets

    stats = open(directory + "/NEW/lengths.csv", 'w')
    f = csv.writer(stats, delimiter=',')

    with open(directory+"/"+file) as i_file:
        for line in i_file:
            total_N += 1
            full_text = json.loads(line)["full_text"]
            full_text_length = len(full_text)
            total_length += full_text_length
            flag_you = 0
            flag_hashtags = full_text.count("#") # other ways to count hashtags?
            if flag_hashtags > 3:
                flag_hashtags_N
            if "you" in full_text.lower():
                flag_you_N += 1
                flag_you = 1
            f.writerow([str(full_text), str(full_text_length)])

    print("Total tweets: " + str(total_N))
    print("Average length: " + str(total_length/total_N))

def sourceInfo(directory, file):

    stats = open(directory + "/NEW/sourceInfo.csv", 'w')
    f = csv.writer(stats, delimiter=',')
    f.writerow(["retweet_count", "favorite_count", "quote_count", "reply_count"])

    for (dirpath, dirnames, filenames) in os.walk(inputFolder):
        for filename in filenames:
            if filename.endswith('.json'): 
                print("Currently on " + filename)
                with open(dirpath+"/"+filename) as i_file:
                    t = json.loads(line)
                    f.writerow([str(t["retweet_count"]), str(t["favorite_count"]), "unknown", "unknown"])

def main(argv):
    print("\nRunning...")
    # lengths(argv[0], argv[1])
    sourceInfo(argv[0], argv[1])

if __name__== "__main__":
    main(sys.argv[1:])