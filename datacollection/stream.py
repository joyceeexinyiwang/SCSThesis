"""

COMMANDS:
source activate thesis
python stream.py queries.csv

"""


import csv, sys, time, os
from datetime import datetime
import credentials as cred
import stream_tools
from credentials import getAuth

def run(queryFile):

    #Create Query list
    queries = ""
    with open(queryFile) as i_file:
        queries = i_file.read()
    queries = queries.split(",")

    key = "hello"
    uKey ="Thesis"
    i = 1
    quer = ["hello"]

    print('Streaming for ' + key)

    ckey = cred.cred_dict[uKey]['ckey'][i]
    csecret = cred.cred_dict[uKey]['csecret'][i]
    atoken = cred.cred_dict[uKey]['atoken'][i]
    asecret = cred.cred_dict[uKey]['asecret'][i]

    auth = getAuth(i)
    # auth = None

    now = datetime.now()
    out_Path = "streamData/" + now.strftime("%Y-%m-%d-%H-%M")
    stream_tools.stream_tweets(auth, key, quer, out_Path, ckey, csecret, atoken, asecret)


def main(argv):
  print("Running stream.py")
  run(argv[0])
  
if __name__== "__main__":
  main(sys.argv[1:])