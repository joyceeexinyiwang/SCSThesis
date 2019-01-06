This module is updated by Joyce Wang (xinyiw).  
Originally based an existing moduled created by rvillaco on Thu Oct 4 17:23:35 2018.

---

#### General

To stream data:  
`python stream.py keywords.csv appNumber`

To scrape with multiple keywords:  
`python scrape.py keywords.csv outputFolder maxTweets appNumber`

To scrape using one single keyword:  
`python one.py keyword outputFolder appNumber`

To deduplicate:  
`python clean.py dedup inputFolder outputFileName`

To separate by date:
`python clean.py date inputFolder outputFileName` (NOT FINISHED)


Other functions:  
`python func.py tweetID appNumber`

--- 

#### Related to news

To do a naive query of the retweet/quote/reply network of a specific tweet:  
- retweet: query by keywords of original tweets and filter
- quote: query by url and filter
- reply: query by news agency handle and filter
`python tweet_network.py keywords.tsv outputFolder appNumber` (retweets and quotes)  
`python one.py newsAgencyHandle outputFolder appNumber` (query by handle)  
`python replies.py ids_file inputFolder outputFolder loops` (filter to get replies NEED FIXES)  
`python clean.py dedup inputFolder outputFileName` (dedup)

To get sentiments:  
`python sentiments.py inputFolder outputFileName`

To query and profile agents of tweets:  
`python agents.py inputFolder outputFileName`

---

(for Joyce only)  
To switch into the `thesis` environment:  
`source activate thesis`

