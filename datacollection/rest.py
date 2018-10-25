# -*- coding: utf-8 -*-

"""
python -m site --user-site
/Users/xinyiwang/.local/lib/python3.6/site-packages

COMMANDS:
source activate thesis
python rest.py queries.csv 1000

"""

import datetime, sys
import tweepy
from credentials import getAuth
from rest_tools import rest_scrape

def run(qFile, maxTweets):   

    #Create Query list
    queries = ""
    with open(qFile) as i_file:
        queries = i_file.read()
    queries = queries.split(",")

    i = 0

    auth = getAuth(i, "app")
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    now = datetime.datetime.now()
    out_Path = "data/" + now.strftime("%Y-%m-%d-%H-%M") + "-scrape"

    ## Start Scrapping
    print ('## Running scrape \"{keywords}\" on app #{a})'.format(keywords=str(queries), a=i))
    ScrapeResults=rest_scrape(queries, api, out_Path, int(maxTweets))


def main(argv):
  print("Running")
  # queries, maxTweet
  run(argv[0], argv[1])
  
if __name__== "__main__":
  main(sys.argv[1:])
