import csv, sys, time, os
from datetime import datetime
import tweepy
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
import credentials as cred
import stream_tools

class listener(StreamListener):
    def __init__(self, path, fileName,StartDate):
        StreamListener.__init__(self)
        self.fileName=r'{0}/{1}'.format(path,fileName)
        self.start_date=StartDate        
        self.base_file=open(r'{0}.json'.format(self.fileName),'a+',encoding="utf8")

    def on_data(self, data):
        print("on_data")
        today=datetime.now().strftime("%Y-%m-%d")
        if today!=self.start_date:
            self.start_date=datetime.now().strftime("%Y-%m-%d-%H-%M")
            self.base_file.close()
            fName=r'{0}_{1}.json'.format(self.fileName,self.start_date)
            self.base_file=open(fName,'a+',encoding="utf8")
            print('Day expired, now writing in file: ' + fName)
        self.base_file.write(data)
        return True

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

def fetch(auth, query,outPath,fileName,ckey,csecret,atoken,asecret,max_daily_errors=5):

    startDate=datetime.now().strftime("%Y-%m-%d")
    error_per_day=0
    timeOfFirstError=None
    sListenter=listener(outPath,fileName,startDate)

    twitterStream = Stream(auth=auth, listener=sListenter)
    print('Starting Stream')
    twitterStream.filter(track=query)
    while True:
        try:
            print('...', end="")
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
        time.sleep(0.1)

def stream_tweets(auth, seachedKey,query_list,outPath,ckey,csecret,atoken,asecret):
    if not os.path.exists(outPath):
        os.makedirs(outPath)
    fName='{0}'.format(seachedKey)
    fetch(auth, query_list,outPath,fName,ckey,csecret,atoken,asecret)