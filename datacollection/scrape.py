# -*- coding: utf-8 -*-

"""
$ source activate thesis
$ python scrape.py queries/AJEEnglish_Khashoggi.csv 100000000 0
$ python scrape.py queries/AP_Khashoggi.csv 100000000 1
$ python scrape.py queries/AP_tol.csv 100000000 2
$ python scrape.py queries/PittsburghPG_tol.csv 100000000 1


"""

import datetime, sys
import tweepy
from tools import credentials as cred
from tools import rest_tools as rest
from tools import clean

def run(qFile, maxTweets, appN):   

    #Create Query list
    queries = ""
    with open(qFile) as i_file:
        queries = i_file.read()
    queries = queries.split(",")

    qFilename = qFile[qFile.rindex("/"):qFile.index(".")]
    print ("## Running scrape on file {a}".format(a=qFilename))

    i = int(appN)

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
  # queries, maxTweet, app number
  run(argv[0], argv[1], argv[2])
  
if __name__== "__main__":
  main(sys.argv[1:])
