import tweepy

#Credentials
cred_dict={'Thesis':{'ckey':[],'csecret':[],'atoken':[],'asecret':[]}} #Create Dictionary for each account
cred_dict['Thesis']['ckey']=["oGymKwaEmMih2Evpvpf6OdM5L", "TAYFiq08g0dJRaOKJ1pjGypVA", "ntXOwYjbkWvM5kWwRGsWYlvle"] #I use lists as I have multiple apps per account
cred_dict['Thesis']['csecret']=["azWdvSiYYi1ciIYqXh8D8Z1IzAUFGrR4pMr7srLNiZe7leUe9V", "mTL3hxg9KkXdAUwczb4hCEj9LTRvez20ywxzlAV1cxddAETXXe", "52f3l6Sx4j2zrs7xcjb4PNOuxnGCnjkUCG6XHQf2FuJ4T6G2ne"]
cred_dict['Thesis']['atoken']=["1051549838792364035-t2PvjyeXW3UIsQuH7l00MxdhXxYReD", "1051549838792364035-TuVg6QFOYhBlGKYfHM7sj60guO1xCc", "1051549838792364035-ThZ0KsVBTVFWVebOumlY7ZLG0iEJTT"]
cred_dict['Thesis']['asecret']=["ob7MhEOhFykrggxvPpxc8qnjE0aO9xSrVY9UgIhFRG1m1pr", "k9ua4w2PH3d6BSYvLfaFjaJCmVg5mZ0tjT0wXGezQwlzH", "HXGsnXHvGZcztssvz4qmV76MVk171K6AOfP8EYVCXNsyQ"]


### App-User Authorization

def getAuth(i):
    ckey = cred_dict['Thesis']['ckey'][i]
    csecret = cred_dict['Thesis']['csecret'][i]
    atoken = cred_dict['Thesis']['atoken'][i]
    asecret = cred_dict['Thesis']['asecret'][i]
    auth = authorizer(ckey,csecret,atoken,asecret)
    return auth


def authorizer(ckey,csecret,atoken=None,asecret=None):
    """
    Ramon:
    :mode: either "user" or "app". "user" requires access tokens also.
    :return: corresponding API authorization
    """
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret) 

    return auth
