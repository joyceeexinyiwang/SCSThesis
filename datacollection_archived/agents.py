# -*- coding: utf-8 -*-

"""
$ source activate thesis
$ python agents.py inputFolder appNumber

"""

import datetime, sys
import tweepy
from tools import credentials as cred
from tools import rest_tools as rest
from tools import clean

def run(handle, qFile, maxTweets, appN):   

    #Create Query list
    qlist = ""
    with open(qFile) as i_file:
        qlist = i_file.read()
    qlist = qlist.split(",")

    queries = []

    for q in qlist:
        queries.append(handle + " " + q)

    qFilename = qFile[qFile.rindex("/")+1:qFile.index(".")]
    print ("## Running scrape on file {a}".format(a=qFilename))

    i = appN

    auth = cred.getAuth(i, "app")
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    now = datetime.datetime.now()
    path = "data/" + handle + "_" + qFilename + "/" + now.strftime("%Y-%m-%d-%H-%M")

    ## Start Scrapping
    print ('## Running scrape \"{keywords}\" on app #{a})'.format(keywords=str(queries), a=i))
    ScrapeResults=rest.rest_scrape(queries, api, path + "/by_keywords", int(maxTweets))

    ## Clean up

    i = appN

    auth = cred.getAuth(i, "app")
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def main(argv):
  print("")
  # inputFolder app number
  run(argv[0], int(argv[1]))
  
if __name__== "__main__":
  main(sys.argv[1:])
