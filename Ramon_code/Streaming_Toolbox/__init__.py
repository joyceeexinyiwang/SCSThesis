# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 16:51:32 2018

@author: User
"""
from .Stream_Tools import *
from .REST_Tools import *
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
cred_dict['CMU']['ckey']=["oGymKwaEmMih2Evpvpf6OdM5L", "TAYFiq08g0dJRaOKJ1pjGypVA"] #I use lists as I have multiple apps per account
cred_dict['CMU']['csecret']=["azWdvSiYYi1ciIYqXh8D8Z1IzAUFGrR4pMr7srLNiZe7leUe9V", "mTL3hxg9KkXdAUwczb4hCEj9LTRvez20ywxzlAV1cxddAETXXe"]
cred_dict['CMU']['atoken']=["1051549838792364035-t2PvjyeXW3UIsQuH7l00MxdhXxYReD", "1051549838792364035-TuVg6QFOYhBlGKYfHM7sj60guO1xCc"]
cred_dict['CMU']['asecret']=["ob7MhEOhFrggxvPpxc8qnjE0aO9xSrVY9UgIhFRG1m1pr", "k9ua4w2PH3d6BSYvLfaFjaJCmVg5mZ0tjT0wXGezQwlzH"]

