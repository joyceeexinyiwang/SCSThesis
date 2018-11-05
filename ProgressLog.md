
## To-do

*scope down to some specific research questions and start defining some hypothesis.*

**Approach 1: Tracing threads** 
- Read a sample of individual tweets to make some empirical observations and understand what exactly people tend to write
- find patterns of how information gets passed on as a news story unfolds

**Approach 2: DNA**
- mention/retweets/quote/reply networks
- friends and followers networks
  - understand the different types of agents in the tweets I collected (influencers? journalists? followers of the news agency? bots?)

- get ORA pro
- read "Statistical Analysis of Network Data"
- read DNA book

Curious: 
> when the news cycle around Jamal Khashoggi dies down, who is still talking about it, and how are they talking about it?

> read papers (existing knowledge!!)


---


### Fri 11/9/2018
### Thu 11/8/2018
### Wed 11/7/2018
**put some numbers behind the observations.**
To assess the opinion strength of the message you could use these indicators
a) use of emotional words
b) use of bold letters
c) use of capitals
d) use of excalamation points

### Tue 11/6/2018
- profile agents and scrape agent data
- analyze ORA report

### Mon 11/5/2018
profile agents by 
- profession (news orgs, individual journalist, and others, by [verified status](https://help.twitter.com/en/managing-your-account/about-twitter-verified-accounts) and account description)
- influence (high/mid/low profile, by follower number)
- activeness (how frequently they post on Twitter)
some example types
- POTUS (other, high profile, active)
- NYTimes (news orgs, high profile, active)
- [@ArturoFernandez](https://twitter.com/ArturoFernandez) (individual journalist, mid profile, active)
- [Pittsburgh Jewish Chronicle](https://twitter.com/PittJewishChron) (news orgs, mid profile, active)
- [carolyn limnyuy](https://twitter.com/CarolineBeriny1) (other, low profile, active)
> which kinds of agents are most common?  
> how do these agents interact with each other? 

---

## Past


### Mon 11/5/2018
- scrape tweets [@AP, @AJEnglish] x [event keywords]
- [Glossary of graph theory terms](https://en.wikipedia.org/wiki/Glossary_of_graph_theory_terms#Walks)

### Sat 11/3/2018
- read papers

### Fri 11/2/2018

improved thread.py
- print retweet, quote, reply (from a particular tweet, going *backward*)

**Empirical observations**: narratives of information threads
  - (from 10/26/2018) some times a person would address multiple news agencies at the same time in a tweet. "@AJEnglish @newsweek blah blah blah..." (e.g. tweet id 1054414678619815938)
  - (from 10/26/2018) accounts with low follower counts issue strong opinions 
  - many journalists tend to help spread the words
  - discourse often starts with news articles and evolve into larger scope (needs proof)
  - people mentioning make comparisons between concurrent events ('Don Mathews 🌊': '@AP_Politics @AP It [Trump visiting Pittsburgh] reminds me of the Saudi prince inviting Khashoggi’s son to the Palace') 
  - ??? when someone mentions a news corp, does the news corp decide to respond???

data collection issues:
- @AP includes a bunch of unrelated users and tweets


### Wed 10/31/2018
- wrote thread.py to get short threads of interactions

### Tue 10/30/2018
- wrote dedup.py, clean.py, and bydate.py


### Mon 10/29/2018
- read texts
- started user.py, dedup.py, bydate.py

### Sun 10/28/2018

influencer v.s. non-influencer  
agreement v.s. disagreement  
reaction v.s. reiteration  

mentioning: reaction, disagreement  
retweeting: agreement, replication  
number of followers and verified status: influencer/non-influencer status  
centrality measures: 

*how do these things change over time?*  
*how to trace the spread of one specific piece of information that stems from a news agency? (which kind of information has the deepest/longest thread? which has the broadest/widest? )*  

(meta-analysis, not focusing on specific opinions, but on the exchange of opinions)  


### Fri 10/26/2018
Twitter API truncate issue: 
- similar problem: https://twittercommunity.com/t/retrieve-full-tweet-when-truncated-non-retweet/75542
- answer: https://developer.twitter.com/en/docs/tweets/tweet-updates.html
- answer: https://github.com/tweepy/tweepy/issues/878

`results = api.search(q=query, lang=language, count=tweetCount, tweet_mode='extended')  
for tweet in results:  
        print(tweet.fulltext)`

**apparently not working for retweet??**

From reading individual tweets, I saw that
- some times a person would address multiple news agencies at the same time in a tweet. "@AJEnglish @newsweek blah blah blah..." (e.g. tweet id 1054414678619815938)
- accounts with low follower counts issue strong opinions  

*How many people who engage in this stuff is an influencer?*  
*How many people are not influencers?*  
*What are the different impacts of influencers and non-influencers on the community? (define influencer based on follower counts? people non-influencers tend to express opinions more? influencers get more retweets? non-influencers get more followers when they issue opinions?)*

*how do those who agree with the news stories and those who don't behave differently? (hypo: agreement gets more retweets, disagreements add more personal opinions, disagreements come from non-influencers --> echo chambers)*
- other sources that prove the following hypothesis?
  - people who agree tend to retweet more than other forms of interactions
  - people who disagree tend to reply, comment, or @ their target news agencies
  - agreement behaviors tend to come from a wide range of people
  - disagreement baheviors tend to come from a small number of non-influencers


### 10/25/2018 *Meeting with Matt*

ORA
- friends/followers networks
- ask/mention/retweet networks
- each node: new agency? journalist? bots?
  - can add additional attributes to each Agent
- ORA generates reports

Stories behind interactions
  - read individual tweets in Excel
  - examine how individual agents interact with the new stories
  - group dynamics v.s. individual behaviors

[How Humans versus Bots React to Deceptive and Trusted News Sources: A Case Study of Active Users](https://arxiv.org/abs/1807.05327)

talk to Dave: network changes over time


### 10/17/2018
adapted Ramon's code to collect 


### 9/19/2018
“Computing Political Preference among Twitter Followers”  
"What Journalists Share: A Comparative Study of the National Press Corps in Australia and Germany"  
["Who’s behind that tweet? Here’s how 7 news orgs manage their Twitter and Facebook accounts"](http://www.niemanlab.org/2014/05/whos-behind-that-tweet-heres-how-7-news-orgs-manage-their-twitter-and-facebook-accounts/#disqus_thread) via Neiman Lab
> According to this Neiman Lab article, tweets with voices tend to generate the most interactions. Maybe consider **voice/no voice** as one of the distinguishing factors for social media-based journalistic behavior?

> This article is from 2014 and most news outlets had a manual component to their Twitter. However, as NLG technologies become more advanced these days, is the real personal voice still necessary? Are they using generated personal voices now?

> Without knowing the automation mechanisms behind news corps Twitter accounts, how to distinguish between journalistic practices and understand their rippling effect?

### 9/17/2018
"Modeling and Predicting News Consumption on Twitter"  
Found Medium publication ["Journalism Trends and Technologies: White Papers on Key Trends in Journalism"](https://medium.com/journalism-trends-technologies).  
Found ["Journalism,"Fake News" & Disinformation: Handbook for Journalism Education and Training"](http://unesdoc.unesco.org/images/0026/002655/265552E.pdf) as part of UNESCO Series on Journalism Education (via [Neiman Lab article](http://www.niemanlab.org/2018/09/fighting-back-against-fake-news-a-new-un-handbook-aims-to-explain-and-resist-our-current-information-disorder/?utm_source=Daily+Lab+email+list&utm_campaign=a2dcdf2ff7-dailylabemail3&utm_medium=email&utm_term=0_d68264fd5e-a2dcdf2ff7-396323673)).

### 9/14/2018
["Pay Models for Online News"](https://medium.com/journalism-trends-technologies/pay-models-for-online-news-8ea87d46a3c7#_ftn1)

### 9/13/2018
["Xinhua to integrate AI into news production"](http://www.xinhuanet.com/english/2018-01/09/c_129786724.htm)

### 9/12/2018
"Finding News Curators in Twitter"  
"Engage Early, Correct More: How Journalists Participate in False Rumors Online During Crisis Events"  
"Sourcing and Trust: Twitter Journalism in Ireland"  

### 9/11/2018
Watched [videos](http://netanomics.com/ora-video-training-guides/) about ORA

### 9/9/2018
> Paper structure: relates works, framework, case studies, discussion, process and methods

### 9/7/2018
"Engage Early, Correct More: How Journalists Participate in False Rumors Online During Crisis Events" (CHI 2018)
> I can have a list of research questions and hypotheses in my paper, and tackle them individually but (hopefully) within the same process/framework

### 9/6/2018
D&S: "The Promises, Challenges, and Futures of Media Literacy"  
D&S: "Searching for Alternative Facts: Analyzing Scriptural Inference in Conservative News Practices"  
> - research on Youtube data could really benefit from video analysis technologies like what Will Crichton works on  
> - annotation scheme: network of interlocutors (forwarding, featuring, etc)  
> - how to formally characterize the behaviors of news accounts?  
> - How to detect patterns that consistently stand regardless of algorithms? Or meta-patterns of algorithms? We don't want to patterns to be useless when platforms change their design.  

### Summer 2018
- Carley, Kathleen M., Guido Cervone, Nitin Agarwal, Huan Liu. "Social Cyber-Security." [link](http://www.casos.cs.cmu.edu/events/summer_institute/2018/si_portal/pubs/Carley%20-%20Social%20Cyber%20Security.pdf)
  - general overview of the field of social cyber-security
- Balconi, Margherita, Stefano Breschi, and Francesco Lissoni. "Networks of inventors and the role of academia: an exploration of Italian patent data." Research Policy 33, no. 1 (2004): 127-145. [link](/docs/Balconi-2003.pdf)
  - proprietory science and technology in academic and industry
- Abbasi, Alireza, Liaquat Hossain, and Loet Leydesdorff. "Betweenness centrality as a driver of preferential attachment in the evolution of research collaboration networks." Journal of Informetrics 6, no. 3 (2012): 403-412. [link](/docs/Abbasi-2012.pdf)
  - social networks underlying the co-authorships between new authors and already-published authors
- Balland, Pierre-Alexandre. "Proximity and the evolution of collaboration networks: evidence from research and development projects within the global navigation satellite system (GNSS) industry." Regional Studies 46, no. 6 (2012): 741-756. [link](/docs/Balland-2010.pdf)
  - the connection between proximity of organizations and the tendency for collaboration between them
  - I was confused about the algorithms
- Girvan, Michelle, and Mark EJ Newman. "Community structure in social and biological networks." Proceedings of the national academy of sciences 99, no. 12 (2002): 7821-7826. [link](/docs/Girvan-2002.pdf)
  - new approach to detect clustering (communities) in social networks
  - using edge-betweenness to detect community peripheries
- Kathleen M. Carley, 1990, “Structural Constraints on Communication:  The Diffusion of the Homomorphic Signal Analysis Technique through Scientific Fields,” Journal of Mathematical Sociology, 15(3-4): 207-246. (can't download online) 

*vocab: centrality (degree, betweenness, and closeless), network analysis, geodesic distance, distance and proximity.*

#### ORA
- downoad the university version of ora from the casos web site
- watch these videos: http://netanomics.com/ora-video-training-guides/
- sampe data sets: http://www.casos.cs.cmu.edu/tools/data.php
- academic version of ora: http://www.casos.cs.cmu.edu/projects/ora/download.php
- ORA Description Final.pdf [link](https://github.com/joyceeexinyiwang/SocietalComputing/blob/master/docs/ORA%20Description%20Final%20-%202017.pdf)
- ORA QuickStart Guide v3.pdf [link](https://github.com/joyceeexinyiwang/SocietalComputing/blob/master/docs/ORA%20QuickStart%20Guide%20v3.pdf)
