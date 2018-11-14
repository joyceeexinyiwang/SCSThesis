# -*- coding: utf-8 -*-

"""
$ source activate thesis

$ python scrape.py PittsburghPG queries/tol.csv 100000000 1
$ python scrape.py AP queries/tol.csv 100000000 2


TODO:

$ python scrape.py PittsburghPG queries/tol.csv 100000000 1
$ python scrape.py AP queries/tol.csv 100000000 2

$ python scrape.py nytimes queries/thousandoaks.csv 100000000 0
$ python scrape.py washingtonpost queries/thousandoaks.csv 100000000 3
$ python scrape.py latimes queries/thousandoaks.csv 100000000 1

$ python scrape.py nytimes queries/woolseyfire.csv 100000000 4
$ python scrape.py latimes queries/woolseyfire.csv 100000000 5
$ python scrape.py ap queries/woolseyfire.csv 100000000 6


Move to data folder on drive

$ python scrape.py nytimes queries/thousandoaks_small.csv 100000000 3
$ python scrape.py washingtonpost queries/thousandoaks_small.csv 100000000 3



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

    i = (appN + 1)%4

    auth = cred.getAuth(i, "app")
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    allTweets = clean.dedup(path + "/by_keywords", path + "/cleaned", "deduped.json")
    (relevantTweets, irrelevantTweets) = clean.filter(path + "/cleaned", "deduped.json", path + "/cleaned", handle, maxTweets, appN)
    relevantTweets = clean.dedupFile(path + "/cleaned/relevant.json", path + "/cleaned", "deduped_relevant.json")
    clean.separateByDate(relevantTweets, path + "/by_dates")


def main(argv):
  print("")
  # news agency, queries, maxTweet, app number
  run(argv[0], argv[1], int(argv[2]), int(argv[3]))
  
if __name__== "__main__":
  main(sys.argv[1:])
