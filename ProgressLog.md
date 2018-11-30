## NEW APPROACH
*How to describe the evolving relationship between the news org, the journalist, and the audience?*

In print, there is a more linear relationship from news creation (news agencies and journalists) to news consumption (readers). With social-media, the relationship between news professionals and their readers become more convoluted. Once content is created and posted on the web, news orgs, journalists, and readers interact with each other to spread the information and engage in discourse. Original content gets shared as a link in the tweet, most often by the news orgs themselves. 

I want to explore the different kinds of links between these different roles, and paint a quantified picture of how news get spread around between different agents, which would help illustrate the complex relationship between news professionals and readers nowadays.

Informational influence across different types of agents?

**Game plan**:
- annotate all agents
  - find an event, collect agent data, annotate them to be news org, journalist, or citizen (is this new much?)
  - down the line can profile agents based on: bots, influence, etc.
- build network based on following **relationship framework**
  - link -> org
  - link -> journalist
  - link -> reader
  - news org <- news org
  - news org <- journalist
  - news org <- reader
  - journalist <- news org
  - journalist <- journalist
  - journalist <- reader
  - reader <- journalist
  - reader <- reader
- analyze ORA reports:
  - which agents are most active?
  - which relationships are most common?
- with each agents:
  - who follow them and who do their followers follow?
  - in their tweets, do they...
    - "spread information" (link sharing, non-sentiment retweets, etc.) v.s. "spread opinion" (opinion, sharing opinion links, sharing opinion tweets, etc.) v.s. "express opinion" (reply, opinion tweets, etc.)
  - describe their informational influence based on follower-network and behavior
    - **what's the reach if they "spread information"?**
    - **what's the reach if they "spread opinion"?**
    - **what's the reach if they "express opinion"?**
  - how do informational influence differ among news orgs, journalists, citizen journalists, and citizens based on the above metrics?
- connect back to news events:
    - vertical stories?
- hypothesis
  - news orgs spread their original content the most
  - journalists prefer to share their orgs' content rather than share links on their own
  - readers prefer retweet rather than share direct links of news articles
  - readers prefer to share tweets that do not have comments
  - journalists tweet less but reach a farther group of people
- **visualize** the dissemination of news and the relationships of agents in a graph (similar to journal entry 11/28/2019)

Future questions:
- Does the Twitter community have the power to influence whether people think of an article as good or bad? Does a negative comment increase its retweeting numbers? (The self-correcting power of the community)
- Who reads People's Daily on Twitter? (I can use the strategies developed in this work and see if People's Daily shows peculiar patterns that are at odds with new media in the 'free' world.)


## APPROACH 2

News orgs, citizens, influential individuals, non-influential individuals:
- **What's their reach if they "spread information"?**
- **What's their reach if they "spread opinion"?**
- **What's their reach if they "express opinion"?**

- classify the type of information: "spread information" (link sharing, non-sentiment retweets, etc.) v.s. "spread opinion" (opinion, sharing opinion links, sharing opinion tweets, etc.) v.s. "express opinion" (reply, opinion tweets, etc.)
  - sentiment analysis
  - how to perform sentiment analysis over content of links?
- classify reach: number of retweets and likes and snowballing, the type of people that these content reach
  - build my own meta-network?
  - correctly identify journalists and citizen-journalists
- choose an agent, analyze informational influence for three types of informational spread
- look at other agents



#### To-do:

build custom networks and analyze reports

- read related works and organize
  - what we know already about the relationship graph:
    - journalists and news curators...
    - ...
  - information influence and responsibility
- finish reading reports and come up with a few observations
- agent data and annotation


---

### Friday 11/30/2018

Meeting with Matt:
- go over research approach
- netmapper/sentiment analysis
- detect bot
- poster presentation (data collection, related works, framework, observations, future plan)
- how to build custom networks

### Thursday 11/29/2018
Meeting with David Danks
- (my project started from a place where I am interested in helping people take better responsibility over the weight and influence of their words)
- information influence of agents in the context of news consumption
- responsibility: can we allow agents to self-monitor their role in the network?
  - what is the accountability of an agent...
    - as a reader, filter their own sources and spread the words forward 
    - understand their role as a channel?
    - ...how to if they cannot exactly predict where their words go?
    - what they do is: understand their own proximities--sources/audiences
    - provide a new lens to look at informational influence?

Readings
- "News sharing in social media: The effect of gratifications and prior experience": the uses and gratifications (U&G) and social cognitive theories (SCT), how influences of information seeking, socializing, entertainment, status seeking and prior social media sharing experience on news sharing intention
- "Posting, commenting, and tagging: Effects of sharing news stories on Facebook": asking the network’s opinions and targeting specific friends led to greater involvement in the news content; discussion through comments led to a greater sense of influence and greater involvement for those sharing the news story
- "Share, Like, Recommend" (Hermida, 2012): based on an online survey of 1600 Canadians
  - Two-fifths of social networking users said they receive news from people they follow on services like Facebook, while a fifth get news from news organizations and individual journalists they follow.
  - a significant number of social media users value their personal network as a way to filter the news, rather than solely relying on the professional judgment of a news organization or journalist.
  - a message from a news organization or journalist was sent on average 15.5 times (An et al., 2011)
  - **useful stats table: use of social media for news and information on a typical day (%)**
  - Canadians were twice as likely to prefer news links and recommendations from friends and family than from journalists or news organizations on both Facebook and on Twitter. While, as has been cited, 43 per cent said they received their news from friends and family on social networks like Facebook, only 20 per cent cited the account of a news organization or a journalist as a source.
  - On Twitter, only 10 per cent of social media users said they followed a journalist or news outlet, compared to 18 per cent from personal connections.
- "Ideological Segregation and the Effects of Social Media on News Consumption" (Flaxman, 2013): examining web browsing histories for 50,000 U.S.-located users who regularly read online news
  - these polarizing articles from social media and web search constitute only 2% of news consumption. Consequently, while recent technological changes do increase ideological segregation, the magnitude of the effect is limited.
  - classify news v.s. opinion pieces based on words in url using machine learning
- "Reuters Institute Digital News Report 2017":
  - "incidental exposure to news" – situations where people end up consuming something while intending to do something else.
  - For users of both social media and news aggregators, more people agree that they often see news from sources they wouldn’t normally use (36% and 35%) than disagree (27%). As a possible consequence of this, but also because these services have the potential to incidentally expose users to different topics as well as different news sources, more agree (40% and 37%) that they often see news stories that do not interest them than disagree (27%).
  - **A significant number of people across all 36 markets say that they curate their social feeds based on the news content they want to see**. Over a third (36%) have added a user for news, and around one in five have blocked someone because of news they posted. A similar number have also fine-tuned their feeds in order to see more or less news from a particular account.
  - So far we have seen that only a minority of users share and comment on news in most countries. To understand why most people tend to abstain from sharing and commenting on news, we asked them to identify possible reasons why. When looking at overall findings, we find that the two most cited reasons are (a) lack of interest in commenting on news and sharing news (37%) and (b) a preference for face-to-face discussions (37%).

### Wednesday 11/28/2018

(See graph on journal entry of 11/28/2018)

---

### Plans archived on 11/28/2018

**Approach 1: Tracing threads** 
- Read a sample of individual tweets to make some empirical observations and understand what exactly people tend to write
- find patterns of how information gets passed on as a news story unfolds

**Approach 2: DNA**
- mention/retweets/quote/reply networks
- friends and followers networks
  - understand the different types of agents in the tweets I collected (influencers? journalists? followers of the news agency? bots?)

Curious: 
> when the news cycle around an event dies down, who is still talking about it, and how are they talking about it?

- Find vertical stories (threads of tweets on a micro scale) and horizontal stories (propagation of tweets on a macro scale)
- Collect data on ToL, Thousand Oaks, Woolsey fire

To prove quantitatively:
- journalists (especially those who work for the news org) spread the words most effectively --> because their high follower count and that their followers probably share similar views?
- many accounts with low follower counts express very strong and controversial opinions and stir the pot on a smaller scale
- many people like to address multiple news agencies at the same time in a tweet. e.g., "@AJEnglish @newsweek blah blah blah..."
- mentioning seems to be associated with strong reactions, disagreement; retweeting seems to be associated agreement; quoting seems to be associated with a variety of sentiments

Understanding Agents:
- which kinds of agents are most common?
- how do these agents interact with each other?
- use percentile to set thresholds for influence?
- bot detection
- louvain clustering? (density of topics, density of groups)


---

### Tuesday 11/27/2018

PittsburghPG_tol_1107_Reports observations:
- topic groups
- active agents
- key stories (who tweets what)
- key agents in the stories

local people make the most active and influential agents?

twitter.com/user/status/#id

### Monday 11/26/2018
Louvain clustering -- community detection
- "Tracking the Evolution of Communities in Dynamic Social Networks"
- [Louvain clustering wiki page](https://en.wikipedia.org/wiki/Louvain_Modularity)

tweet classification:
- opinion strength
- rt/quote/reply

To assess the **opinion strength** of the message you could use these indicators  
a) use of [emotional words](https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html#lexicon)  
b) use of all cap words  
c) use of excalamation points  

incorporated Dave's code for sentiment analysis

### Monday 11/19/2018

[Statistics How To](https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/)

use Matt's script to detect news agencies

Measure User Influence:
- [Measuring User Influence in Twitter: The Million Follower Fallacy](https://www.aaai.org/ocs/index.php/ICWSM/ICWSM10/paper/viewFile/1538/1826,2011)
  - findings:
    - 1) popular users who have high indegree are not necessarily influential in terms of spawning retweets or mentions
    - 2) most influential users can hold significant influence over a variety of topics
    - 3) influence is not gained spontaneously or accidentally, but through concerted effort such as limiting tweets to a single topic
  - "Indegree represents popularity of a user; retweets represent the content value of one’s tweets; and mentions represent the name value of a user." ... "retweeting...can typically be identified by the use of RT @username or via @username in tweets...users can respond to (or comment on) other people’s tweets, which we call mentioning. Mentioning is identified by searching for @username in the tweet content, after excluding retweets. A tweet that starts with @username is not broadcast to all followers, but only to the replied user. A tweet containing @username in the middle of its text gets broadcast to all followers."
  - backgrounds: " opinion leaders in the two-step flow theory (Katz and Lazarsfeld 1955), innovators in the diffusion of innovations theory (Rogers 1962), and hubs, connectors, or mavens in other work (Gladwell 2002)"
  - [Spearman's **rank correlation** coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient) --> measure of the strength of the association between two rank sets
  - "The most followed users span a wide variety of public figures and news sources...most retweeted users were content aggregation services (Mashable, TwitterTips, TweetMeme), businessmen (Guy Kawasaki), and news sites (The New York Times, The Onion)...the most mentioned users were mostly celebrities"
  - "To get a measure of influence for a *given topic*, we count only the retweets and mentions a user spawned on the given topic."
  - "For each user, we computed a **single explanatory variable P: the probability that a random tweet posted on Twitter during a 15 day period is a retweet (or a mention) of that user**. Normalizing by the total number of tweets posted on Twitter is essential to cancel out any variable effect on the data and allows the underlying characteristics of the data sets to be compared. For instance, because the Twitter network quadrupled over time in terms of the registered users, the total volume of tweets merely increased over time. Hence, if we didn’t normalize the results, the trend wouldn’t be interesting. Google similarly normalizes the data when analyzing their search trends (Ginsberg et al. 2009)."
- [Classifying Latent User Attributes in Twitter](http://delivery.acm.org/10.1145/1880000/1871993/p37-rao.pdf?ip=128.237.170.101&id=1871993&acc=ACTIVE%20SERVICE&key=A792924B58C015C1%2E5A12BE0369099858%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&__acm__=1542648705_e652767f0dd4e39c7359b1ab6663cf46)
  - stacked-SVM-based classification algorithms over a rich set of original features, applied to classifying gender, age, regional origin, and political orientation
- [Follow the Green: Growth and Dynamics in Twitter Follower Markets](http://delivery.acm.org/10.1145/2510000/2504731/p163-stringhini.pdf?ip=128.237.170.101&id=2504731&acc=ACTIVE%20SERVICE&key=A792924B58C015C1%2E5A12BE0369099858%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&__acm__=1542648728_fcb4a5cf876627e04a630ca19f1bc15a)
- [Everyone’s an Influencer: Quantifying Influence on Twitter](http://delivery.acm.org/10.1145/1940000/1935845/p65-bakshy.pdf?ip=128.237.170.101&id=1935845&acc=ACTIVE%20SERVICE&key=A792924B58C015C1%2E5A12BE0369099858%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&__acm__=1542648733_f1b3735c2c5624eca9c76030e2ac3c1b)


### Friday 11/16/2018
Twitter data research ethics: *Is it okay if we look at individual's tweets and try to profile them as individual human beings?*

Research amplifies data, but is that a voluntary amplification?

### Wednesday 11/14/2018
- collect data on ToL, Thousand Oaks, Woolsey fire
- Some tweets contain an url to a news website, but in the tweet object, the url and the expanded_url are something like "https://t.co/MQcxEaLpwN". Is there a way to detect the source of these urls?

### Tuesday 11/13/2018
[ORA Google group](https://groups.google.com/forum/#!forum/ora-google-group)

### Monday 11/12/2018
Article: "Audience Analysis of Major News Accounts on Twitter" (SocialFlow, 2011)
- written for businesses who want to use social media to reach audiences
- analysis across the Twitter audiences of Al-Jazeera English, BBC News, CNN, The Economist, Fox News and New York Times
- "...we see clear content-based and behavioral differences between audiences: users choose to follow news accounts based on the type of content being posted by the account."

[bot-hunter script](http://data-analytics.net/Apps/botApp/)
- "Note that this model leverages supervised learning and the **training data involves specific bots that attacked NATO in the Summer of 2017**. This means that it is primarily looking for this type of bot, and will not necessarily find many other types."

Generate dynamic networks in ORA:
- when importing Twitter data, aggregate by time
- to generate dynamic reports, make sure the "Meta-Network Time" field is activated
- "Measure Charts" is also helpful for looking at temporal stuff


### Sunday 11/11/2018
half-life of tweets
- Bit.ly has done research in defining half-life of tweets (https://searchenginewatch.com/sew/study/2108186/bitly-links-hour-half-life-study)
- ([link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3278109/)) "The tweeted half-life (THLn) is defined as the point in time after publication by which half of all tweetations of that article within the first n days occur. As n I have used 30 days—that is, as the denominator I chose the total cumulative number of tweets within a 30-day period following the publication date. The THLn is the day when cumulatively half of these tweetations have occurred."
  - "tweetation" = a citation in a tweet (mentioning an article URL), a unit of engagement 
- the article below (Castillo, 2014) has more specific info about half-life 

Article: "Characterizing the Life Cycle of Online News Stories Using Social Media Reactions" (Castillo, 2014)
- RELATED WORKS SECTION: past works surrounding patterns of consumption of online news
  - behavioral patterns of consumption of online news/behavioral-driven article classification
  - prediction of user activities and real-world variables using social media signals (nice table of predictive models in past works)
- classification of articles and their online traffic patterns
- predictive modeling of shelf-life (time passed between its 1rst visit and the time at which it has received a fraction tau of the visits it will ever receive. In this work we set tau = 0:90)
- (Twitter free API only provides partial coverage)
- result: social media signals can improve by a large margin the accuracy of predictions of future visits, as well as the accuracy of predictions of article shelf-life.
- interesting citations: 8, 19, 4, 26, 31, 23, 15, 14

> in the context of news, what is deemed share-worthy by the public? What information is informationally rich but doesn't get shared much?


### Friday 11/9/2018
New events:
- Thousand Oaks shooting data collection (@washingtonpost, @latimes)
- Woosley fires (@washingtonpost, @latimes)

profiling agents **NAIVELY** 
- profession (by whether description contains keywords)
  - keywords = ["news", "newsroom", "columnist", "journalist", "reporter"]
- influence (by sum of followers and friends numbers)
  - "vlow" < 200; 200 <= "low" < 2000; 2000 <= "mid" < 100000; "high" < 100000
- activeness (by number of tweets in the month leading up to the event)
  - "inactive" < 10; 10 <= "active" < 50; "veryactive" > 50 

some example types based on the naive profiling scheme
- POTUS (other, high profile, active)
- NYTimes (news orgs, high profile, active)
- [@ArturoFernandez](https://twitter.com/ArturoFernandez) (individual journalist, mid profile, active)
- [Pittsburgh Jewish Chronicle](https://twitter.com/PittJewishChron) (news orgs, mid profile, active)
- [carolyn limnyuy](https://twitter.com/CarolineBeriny1) (other, low profile, active)


Interesting article: [Reuters’ new algorithm confirms once and for all that Twitter is the best place to find news](https://www.digitaltrends.com/social-media/reuters-algorithm/)
- "biggest (and most important) challenge when developing the algorithm was figuring out what events were newsworthy and not spam"
- Reg Chua, executive editor for data and innovation at Reuters: "We can’t be at everything. Our tool helps shift some of the burden of witnessing and lets journalists do much more of the high value-added work."
- same story covered by [NiemanLab](http://www.niemanlab.org/2016/11/reuters-built-its-own-algorithmic-prediction-tool-to-help-it-spot-and-verify-breaking-news-on-twitter/) and [Columbia Journalism Review](https://www.cjr.org/analysis/cyborg_virtual_reality_reuters_tracer.php) written by computer scientist/journalist [Jonathan Stray](http://jonathanstray.com/me).

### Thu 11/8/2018
ask Dave and Matt for scripts


### Wed 11/7/2018
installed ORA pro

### Tue 11/6/2018
Tried the following data collection approach
- query by url and filter by quote status to get **quotes**
- get all tweets with @newsorg and filter by reply status to get **replies**
- query by a section of the tweet and then filter by retweet status to get **retweets**  

**bug: getting very few tweets**

Ended up using this approach instead
- scrape tweets by keywords
- filter tweets by its tracing back to its origin through a chain of retweet/quote/replay. only keep it if it is relevant to something posted by the news corp in question
- kind of a combination of the keyword-scraping approach and the retweet/quote/reply-scraping approach


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
