import csv, sys, time, os
from datetime import datetime
import credentials as cred
import stream_tools

def run():
    key = "hello"
    uKey ="Thesis"
    i = 0
    quer = ["hello"]

    print('Streaming for ' + key)

    now = datetime.now()
    out_Path = "data/" + now.strftime("%Y-%m-%d-%H-%M")
    stream_tools.stream_tweets(uKey, key, quer, out_Path, 
         cred.cred_dict[uKey]['ckey'][i], cred.cred_dict[uKey]['csecret'][i], cred.cred_dict[uKey]['atoken'][i],cred.cred_dict[uKey]['asecret'][i])


def main(argv):
  print("Running")
  run()
  
if __name__== "__main__":
  main(sys.argv[1:])

