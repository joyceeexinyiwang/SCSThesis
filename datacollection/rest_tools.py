import datetime, time, os, math, json, csv, sys
from collections import Counter
import tweepy

def rest_scrape(terms, tweetAPI, outPath, maxTweets, file_size=500000, fileName=None, max_num_errors=5):
    ''' Perform a REST grab of terms '''
    tweetsPerQry = 100  # this is the max the API permits
    # Number of tweets per file
    file_num=1
    # If results from a specific ID onwards are reqd, set since_id to that ID.
    # else default to no lower limit, go as far back as API allows
    # If results only below a specific ID are, set max_id to that ID.
    # else default to no upper limit, start from the most recent tweet matching the search query.

    if not os.path.exists(outPath):
        os.makedirs(outPath)     
    print("Saving in..." + outPath)
    
    collectedCounts=Counter()
    start_time = time.time()
    count=0
    count_per_file=0
    r'{0}/{1}_log.csv'.format(outPath,fileName)
    logFname=outPath+r'/log.csv'
    if fileName is not None: logFname=r'{0}\{1}_log.csv'.format(outPath,fileName)
    with open(logFname,'a+',encoding='utf8') as outLog:
        logWriter=csv.DictWriter(outLog,['search_term','tweets_downloaded','sinceId'],lineterminator='\n')
        logWriter.writeheader()
        for t in terms:
            #Check whether more than 450 calls have been done before 15 minutes
            errors=0
            sinceId = None
            max_id = -1 
            tweetCount = 0
            print("Downloading max {0} tweets for \'{1}\'".format(maxTweets,t))
            if fileName is not None: nPart='{1}_{2}'.format(fileName, "_".join(t.split(" ")))
            else:   nPart=t
            fname=outPath+r'/{0}_tweets_{1}_max{2}.json'.format("_".join(t.split(" ")), file_num, maxTweets)
            f=open(fname, 'a+',encoding='utf8')
            while tweetCount < maxTweets:
                try:
                    count += 1
                    elapsed_time= time.time() - start_time
                    if count>=449:
                        if elapsed_time<=15*60:
                            print('Tried to do more calls than permited, waiting for {0} seconds'.format(15*60-elapsed_time))
                            time.sleep(15*60-elapsed_time)
                            count=0
                            print('Restarting Stream')
                            start_time = time.time()                
                    if (max_id <= 0):
                        if (not sinceId):
                            new_tweets = tweetAPI.search(q=t, count=tweetsPerQry,tweet_mode='extended')
                        else:
                            new_tweets = tweetAPI.search(q=t, count=tweetsPerQry,
                                                    since_id=sinceId,tweet_mode='extended')
                    else:
                        if (not sinceId):
                            new_tweets = tweetAPI.search(q=t, count=tweetsPerQry,
                                                    max_id=str(max_id - 1),tweet_mode='extended')
                        else:
                            new_tweets = tweetAPI.search(q=t, count=tweetsPerQry,
                                                    max_id=str(max_id - 1),
                                                    since_id=sinceId,tweet_mode='extended')
                    if not new_tweets:
                        print("No more tweets found")
                        logWriter.writerow({'search_term':t,'tweets_downloaded':collectedCounts[t],'sinceId':sinceId})
                        break
                    for tweet in new_tweets:
                        out = json.dumps(tweet._json)
                        f.write(out + '\n')

                    tweetCount += len(new_tweets)

                    print(".." + str(tweetCount) + ".", end='', flush=True)

                    collectedCounts[t]+=tweetCount
                    count_per_file+=len(new_tweets)
                    if count_per_file>file_size:
                        f.close()
                        file_num+=1
                        fname=outPath+r'\{0}_{1}.json'.format(nPart,file_num)
                        f=open(fname, 'a+',encoding='utf8')
                        count_per_file=0
                        
                    #print("Downloaded {0} tweets".format(tweetCount))
                    max_id = new_tweets[-1].id
                except tweepy.TweepError as e:
                    if (errors<=max_num_errors) and (e.api_code==130 or e.api_code==131 or e.api_code==500 or e.api_code==501 or e.api_code==502 or e.api_code==503):
                        errors+=1
                        print('Error #{0}. Status Code {1}. Waiting for {2} seconds'.format(str(errors),str(e.api_code),str(180*errors)))
                        time.sleep(60*errors)
                        continue
                    else:   #Other error                    
                        # Just exit if any error
                        print("#### Breaking stream cause of some unchecked error : " + str(e))
                        break
            print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fname))
    return collectedCounts


def rest_rehydrate(tweet_ids, tweetAPI, outPath, fileName):
    ''' Rehydrate tweets provided in tweet_ids. 
    + fileName: specifies the name of the out file'''   
    
    if isinstance(tweet_ids,set):   list_of_ids=list(tweet_ids)
    else:   
        assert isinstance(tweet_ids,list), 'tweet_ids must be provided on a list or set'
        list_of_ids=tweet_ids

    if not os.path.exists(outPath):
        os.makedirs(outPath)
    #Number of request included
    req_num=math.ceil(len(list_of_ids)/100)
    print('Starting Stream')
    with open(r'{0}\{1}.json'.format(outPath,fileName),'a+') as outTweets:
        with open(r'{0}\{1}_missing.csv'.format(outPath,fileName),'a+') as outLog:
            i=0
            req_count=0
            start_time = time.time()
            for i in range(0,req_num):
                req_count+=1 
                elapsed_time= time.time() - start_time
                if req_count>=449: #The documentation mentions 900 request per 15 minute window (but dont trust it)
                    if elapsed_time<=15.5*60: #The window is 15 minutes, but I add half to play it safe
                        print('Tried to do more calls than permited, waiting for {0} seconds'.format(15*60-elapsed_time))
                        time.sleep(15*60-elapsed_time)
                        req_count=0
                        print('Restarting Stream')
                        start_time = time.time()
                if i%10==0: print('Rehydrating batch # {0} of {1}'.format(i,req_num)) #Notify every 10 batches
                searchTerms=list_of_ids[i*100:(i+1)*100]
                tweets=tweetAPI.statuses_lookup(searchTerms)
                #Write tweets to file and log missing tweets
                collected=set()
                for t in tweets: #Write tweets
                    if 'id_str' in t._json: 
                        id_str=t._json['id_str']
                        collected.add(id_str)             
                    outTweets.write(json.dumps(t._json) + '\n')      
                missing=set(searchTerms)-collected
                for m in missing: #Write Missing tweets
                    outLog.write(m + '\n')  
                i+=1

def get_user_from_name(tweetAPI, **kwargs):
    'Gets User ID from user_id string or screen name'
    user_id=kwargs.pop('user_id',None)
    if user_id is not None: 
        user = tweetAPI.get_user(user_id = user_id)
    else: #Check if user_name is provided
        screen_name=kwargs.pop('screen_name',None)
        if screen_name is not None: 
            user = tweetAPI.get_user(screen_name = screen_name)
        else:
            raise Exception('Need to provide either user_id or user_name')
    return user

def get_timeline(tweetAPI, user_id, directory, pages = 1):
    '''
    Get timeline from user.  Use pages parameter to get up to last 3200 tweets
    in increments of 200 (1 page gives 200, 2 pages gives 400, etc.)
    '''
    import gzip

    timeline = []

    try:
        new_tweets = []
        for page in tweepy.Cursor(tweetAPI.user_timeline, id=user_id, count = 200,tweet_mode="extended").pages(pages):
            new_tweets.extend(page)
        with gzip.open(directory + '/' + str(user_id) + '.json.gz', 'wt') as outfile:
            for tweet in new_tweets:
                timeline.append(tweet)
                out = json.dumps(tweet._json)
                outfile.write(out + '\n')
                timeline.append(tweet._json)
    except tweepy.TweepError as e:
        print(e.reason)

    return(timeline)