# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 17:23:35 2018

@author: rvillaco
"""

from Streaming_Toolbox import cred_dict, rest_scrape
import tweepy
import pandas as pd

#Run Streams    
##### Things to Change ##########

#Server\Laptop Directories
homeDir=r''
out_Path=r'' 


fakeDF=pd.read_csv(homeDir+r'\Data\terms.csv')
fake_terms=list(fakeDF.sort_values('frequency',ascending= False).head(10).term.values) + ['reported']

general_topics=['#HurricaneFlorence', '#Hurricane','Hurricane','Florence', '#Florence','#HurricanePreparedness','#HurricanePrep', '#evacuation','evacuation','FEMA'] 
      
#Create Query Dictionary
queries=[key + " " + l_term for l_term in fake_terms for key in general_topics]

#Scrape Plan
FinalsQueries=[]
Users=list(cred_dict.keys())
scrapePlanFinals={1:{'KEY':Users[0],'App':1,'Queries':general_topics[:5]},
                2:{'KEY':Users[1],'App':1,'Queries':general_topics[5:]},
                3:{'KEY':Users[2],'App':1,'Queries':queries[:20]},
                4:{'KEY':Users[3],'App':1,'Queries':queries[20:50]},
                5:{'KEY':Users[4],'App':1,'Queries':queries[50:80]},
                6:{'KEY':Users[5],'App':1,'Queries':queries[80:]} }

#i=1
#i=2
#i=3
#i=4
#i=5
i=6

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