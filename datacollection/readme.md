This module is updated by Joyce Wang (xinyiw).  
Originally based an existing moduled created by rvillaco on Thu Oct 4 17:23:35 2018.

---

#### General

To stream data:  
`python stream.py keywords.csv appNumber`

To scrape with multiple keywords:  
`python scrape.py keywords.csv outputFolder maxTweets appNumber`

To scrape using one single keywords:  
`python one.py keyword outputFolder appNumber`

To deduplicate:  
`python dedup.py inputFolder outputFileName appNumber`


--- 

#### Related to news on Twitter

To query agents of tweets:  
`python agents.py inputFolder outputFileName appNumber`

To do a naive query of the retweet/quote/reply network of a specific tweet:  
- retweet: query by keywords of original tweets and filter
- quote: query by url and filter
- reply: query by news agency handle and filter
`python tweet_network.py keywords.csv outputFolder appNumber`  
`python one.py newsAgencyHandle outputFolder appNumber`

To get sentiments:  

To get whether the tweets are related to news professionals:  



---

(for Joyce only)  
To switch into the `thesis` environment:  
`source activate thesis`

