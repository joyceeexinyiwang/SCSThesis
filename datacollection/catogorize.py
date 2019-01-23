"""

python categorize.py newsagency inputFolder outputFolder appNumber

categorize into opinion v.s. opinion
get 

"""

import sys, datetime, os, json
from tools import general_tools as gen
from tools import credentials as cred
import tweepy

def categorize(newsagency, inputFolder, outputFolder, appNumber):

def main(argv):
	print("\nRunning...")
	# keyword outputFolder appNumber
	categorize(argv[0], argv[1], argv[2], int(argv[3]))

if __name__== "__main__":
	main(sys.argv[1:])