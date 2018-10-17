from Streaming_Toolbox import cred_dict
from Streaming_Toolbox.Stream_tools import stream_tweets
import csv

#Run Streams    
##### Things to Change ##########

#Server Directories
homeDir=r''
out_Path=r''

#Load Queries for Semis
queries= {}
with open(homeDir+r'\Data\terms.csv',encoding='utf8') as inFile:
    reader=csv.DictReader(inFile)
    for row in reader:
        if row['key'] not in queries: queries[row['key']]=[]
        queries[row['key']].append(row['term'])

#Set Stream Plan
#Days to Stream
available_Users=list(cred_dict.keys())

StreamPlan=[]
i=0
u=0
for k,q in queries.items():
    if u==4:    u=0
    if i<4: appNum=0
    else:   appNum=1
    StreamPlan.append({'Key':k,'uKey':available_Users[u],'appNum':appNum,'query':q})
    u+=1
    i+=1


#Server
#j=0
#j=1
#j=2
#j=3
#j=4
#j=5
#j=6
j=7


########## Start Streaming
key=StreamPlan[j]['Key']
uKey=StreamPlan[j]['uKey']
i=StreamPlan[j]['appNum']
quer=StreamPlan[j]['query']

print('Streaming for ' + key)

stream_tweets(uKey,key,quer,out_Path,cred_dict[uKey]['ckey'][i],cred_dict[uKey]['csecret'][i],cred_dict[uKey]['atoken'][i],cred_dict[uKey]['asecret'][i])
