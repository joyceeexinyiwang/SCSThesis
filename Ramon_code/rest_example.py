# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 17:23:35 2018
@author: rvillaco
"""

# python -m site --user-site
# /Users/xinyiwang/.local/lib/python3.6/site-packages

from Streaming_Toolbox import cred_dict #, rest_scrape
import tweepy
# import pandas as pd

general_topics=['#HurricaneFlorence', '#Hurricane','Hurricane','Florence', '#Florence','#HurricanePreparedness','#HurricanePrep', '#evacuation','evacuation','FEMA'] 
      
#Create Query Dictionary
# search syntax: ' ' == and, ',' == or
queries = general_topics # [key + " " + l_term for l_term in fake_terms for key in general_topics]

#Scrape Plan
FinalsQueries=[]
Users=list(cred_dict.keys())
scrapePlanFinals={1:{'KEY':Users[0],'App':0,'Queries':general_topics[:5]},
	                2:{'KEY':Users[0],'App':1,'Queries':general_topics[5:]}}

i=1

####Finals
Key=scrapePlanFinals[i]['KEY']
appNum=scrapePlanFinals[i]['App']
queries=scrapePlanFinals[i]['Queries']


##Authenticate API
auth = tweepy.AppAuthHandler(cred_dict[Key]['ckey'][appNum],cred_dict[Key]['csecret'][appNum])
api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)

## Start Scrapping
print ('## Running scrape #{0} with user {1} on app # {2})'.format(i,Key,appNum))
ScrapeResults=rest_scrape(out_Path,queries,api)


def main():
  print("Running")
  
if __name__== "__main__":
  main()
