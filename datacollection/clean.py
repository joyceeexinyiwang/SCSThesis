"""

python clean.py dedup inputFolder outputFileName
python clean.py filterByTweet tweetID

"""
import json, sys, os
from tools import basics

def main(argv):
    print("")
    if argv[0] == "dedup":
        # inputFolder outputFileName
        basics.dedup(argv[1], argv[1]+"/clean", argv[2])
    elif argv[0] == "date":
        pass

if __name__== "__main__":
    main(sys.argv[1:])