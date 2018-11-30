"""

Shared with me by Matt:
Dave created this to run textblob, a program that also gives a sentiment score for each tweet in your data.
You input a csv with each row containing the text of a tweet and it outputs sentiments.

"""


import pandas as pd
from textblob import TextBlob
import json, time, io, gzip
import progressbar


out_directory=r""
in_f_name = out_directory+"\\.csv"  #put in file that has list of tweet text


df = pd.read_csv(in_f_name)

#df = pd.DataFrame(data, dtype = str)
    
sent = []
for t in df[df.columns[1]].tolist() :
    text = TextBlob(t)
    sent.append(text.sentiment.polarity)
df['sentiment_score'] = sent
df['sentiment_label'] = df['sentiment_score'].apply(get_sensitivity)
            
df.to_csv('_sentiment.csv', index = False , encoding = 'utf-8')

#
#outfile=open(out_f_name, 'w')
#for user in mixprofiles:
#    outfile.write(json.dumps(user)+'\n') 
#outfile.close()
#

def get_sensitivity(value):
    if value < 0:
        return("negative")
    if value == 0:
        return('neutral')
    else:
        return('positive')