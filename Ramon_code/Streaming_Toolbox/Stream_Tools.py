# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 16:40:20 2018

@author: rvillaco
"""

from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
import time, os
from datetime import datetime


class listener(StreamListener):
    def __init__(self, path,fileName,StartDate):
        self.fileName=r'{0}\{1}'.format(path,fileName)
        self.start_date=StartDate        
        self.base_file=open(r'{0}_{1}.json'.format(self.fileName,self.start_date),'a+',encoding="utf8")
    def on_data(self, data):
        today=datetime.now().strftime("%Y-%m-%d")
        if today!=self.start_date:
            self.start_date=datetime.now().strftime("%Y-%m-%d")
            self.base_file.close()
            fName=r'{0}_{1}.json'.format(self.fileName,self.start_date)
            self.base_file=open(fName,'a+',encoding="utf8")
            print('Day expired, now writing in file: ' + fName)
        self.base_file.write(data)
        return True

def fetch(query,outPath,fileName,ckey,csecret,atoken,asecret,max_daily_errors=5):
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    startDate=datetime.now().strftime("%Y-%m-%d")
    error_per_day=0
    timeOfFirstError=None
    while True:
        try:
            print('Starting Stream')
            sListenter=listener(outPath,fileName,startDate)
            twitterStream = Stream(auth, sListenter)
            twitterStream.filter(track=query)
        except:
            if error_per_day==0:
                error_per_day+=1
                timeOfFirstError=datetime.now()
                print('Error #'+str(error_per_day)+' Waiting for ' +str(60*error_per_day^2)+' seconds')
                time.sleep(60*error_per_day^2)
                continue                
            elif error_per_day<max_daily_errors:
                daysSinceError=(datetime.now()-timeOfFirstError).days
                error_per_day+=1
                if daysSinceError==0:
                    print('Error #'+str(error_per_day)+' Waiting for ' +str(60*error_per_day^2)+' seconds')
                    time.sleep(60*error_per_day^2)
                    continue
                else:
                    error_per_day=1
                    timeOfFirstError=datetime.now()
                    print('Error #'+str(error_per_day)+' Waiting for ' +str(60*error_per_day^2)+' seconds')
                    time.sleep(60*error_per_day^2)
                    continue
            else:
                print('Four errors in the same day, breaking stream')
                sListenter.base_file.close()
                break

def stream_tweets(appName,seachedKey,query_list,outPath,ckey,csecret,atoken,asecret):
    if not os.path.exists(outPath):
        os.makedirs(outPath)
    #Create File name
    fName='{0}_{1}'.format(appName,seachedKey)
    fetch(query_list,outPath,fName,ckey,csecret,atoken,asecret)