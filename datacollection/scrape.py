# -*- coding: utf-8 -*-

"""
$ source activate thesis
$ python scrape.py xxx.csv 100000000

"""

import datetime, sys
import tweepy
from tools import credentials as cred
from tools import rest_tools as rest
from tools import clean

def run(qFile, maxTweets):   

    #Create Query list
    queries = ""
    with open(qFile) as i_file:
        queries = i_file.read()
    queries = queries.split(",")

    qFilename = qFile[qFile.rindex("/"):qFile.index(".")]
    print ("## Running scrape on file {a}".format(a=qFilename))

    i = 1

    auth = cred.getAuth(i, "app")
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    now = datetime.datetime.now()
    out_Path = "data/" + qFilename + "/" + now.strftime("%Y-%m-%d-%H-%M")

    ## Start Scrapping
    print ('## Running scrape \"{keywords}\" on app #{a})'.format(keywords=str(queries), a=i))
    ScrapeResults=rest.rest_scrape(queries, api, out_Path + "/by_keywords", int(maxTweets))

    clean.clean(out_Path + "/by_keywords",  out_Path +  "/by_dates")


def main(argv):
  print("")
  # queries, maxTweet
  run(argv[0], argv[1])
  
if __name__== "__main__":
  main(sys.argv[1:])
