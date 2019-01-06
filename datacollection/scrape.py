# -*- coding: utf-8 -*-

"""
source activate thesis
python scrape.py keywords.csv outputFolder maxTweets appNumber

"""

import sys, datetime
import tweepy
from tools import credentials as cred
from tools import rest_tools as rest
from tools import basics

def run(qFile, outputFolder, maxTweets, appN):   

    # #Create Query list
    qlist = ""
    with open(qFile) as i_file:
        qlist = i_file.read()
        print(qlist)
    queries = qlist.split(",")

    qFilename = qFile[qFile.rindex("/")+1:qFile.index(".")]
    print ("## Running scrape on file {a}".format(a=qFilename))

    i = appN

    auth = cred.getAuth(i, "app")
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    now = datetime.datetime.now()
    path = outputFolder + "/" + qFilename + "_" + now.strftime("%Y-%m-%d-%H-%M")

    ## Start Scrapping
    print ('## Running scrape /"{keywords}/" on app #{a})'.format(keywords=str(queries), a=i))
    ScrapeResults=rest.rest_scrape(queries, api, path + "/by_keywords", int(maxTweets))

    allTweets = basics.dedup(path + "/by_keywords", path + "/cleaned", "deduped.json")
    basics.separateByDate(allTweets, path + "/by_dates")

def main(argv):
  print("")
  # keywords.csv outputFolder maxTweets appNumber
  run(argv[0], argv[1], int(argv[2]), int(argv[3]))
  
if __name__== "__main__":
  main(sys.argv[1:])
