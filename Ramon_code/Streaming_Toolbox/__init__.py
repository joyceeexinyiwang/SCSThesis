# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 16:51:32 2018

@author: User
"""

import tweepy

### App-User Authorization
def authorizer(ckey,csecret,atoken=None,asecret=None,mode='app'):
    """
    :mode: either "user" or "app". "user" requires access tokens also.
    :return: corresponding API authorization
    """    
    if mode == "user":
        auth = tweepy.OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
    
    if mode == "app":
        auth = tweepy.AppAuthHandler(ckey, csecret)        
    return auth

#Credentials
cred_dict={'CMU':{'ckey':[],'csecret':[],'atoken':[],'asecret':[]}} #Create Dictionary for each account
#For CMU Account
cred_dict['CMU']['ckey']=[] #I use lists as I have multiple apps per account
cred_dict['CMU']['csecret']=[]
cred_dict['CMU']['atoken']=[]
cred_dict['CMU']['asecret']=[]

