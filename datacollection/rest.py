# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 17:23:35 2018
@author: rvillaco
"""
"""
python -m site --user-site
/Users/xinyiwang/.local/lib/python3.6/site-packages

COMMANDS:
source activate thesis
python rest.py queries.csv 1000

"""

import datetime, time, os, math, json, csv, sys
from collections import Counter
import tweepy
import credentials as cred
import rest_tools

def run(qFile, maxTweets):   

    #Create Query list
    queries = ""
    with open(qFile) as i_file:
        queries = i_file.read()
    queries = queries.split(",")

    #Scrape Plan
    Users=list(cred.cred_dict.keys())
    scrapePlanFinals={1:{'KEY':Users[0],'App':0,'Queries':queries[0:1]},
                        2:{'KEY':Users[0],'App':0,'Queries':queries[1:2]},
                        3:{'KEY':Users[0],'App':0,'Queries':queries[2:3]}}

    Key="Thesis"
    appNum=0

    ##Authenticate API
    auth = tweepy.AppAuthHandler(cred.cred_dict[Key]['ckey'][appNum],cred.cred_dict[Key]['csecret'][appNum])
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    now = datetime.datetime.now()
    out_Path = "data/" + now.strftime("%Y-%m-%d-%H-%M")

    ## Start Scrapping
    print ('## Running scrape \"{keywords}\" with user {k} on app #{a})'.format(keywords=str(queries),k=Key,a=appNum))
    ScrapeResults=rest_tools.rest_scrape(queries, api, out_Path, int(maxTweets))


def main(argv):
  print("Running")
  # queries, maxTweet
  run(argv[0], argv[1])
  
if __name__== "__main__":
  main(sys.argv[1:])
