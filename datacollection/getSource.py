"""

python getSource.py inputFolder outputFolder agencyHandle appNumber

"""

import sys, datetime, os, json
from tools import general_tools as gen
from tools import credentials as cred
import tweepy

def getSource(inputFolder, outputFolder, appNumber):

	auth = cred. getAuth(appNumber, "app")
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	if not os.path.exists(outputFolder + "/NEW/"):
		os.makedirs(outputFolder + "/NEW/")

	f = open(outputFolder + "/NEW/source.json", "w")

	for (dirpath, dirnames, filenames) in os.walk(inputFolder):
		for filename in filenames:
			if filename.endswith('.json'): 
				print("Currently on " + filename)
				with open(dirpath+"/"+filename) as i_file:

					iDs = set()

					for line in i_file:
						t = json.loads(line)
						

	f.close()


def main(argv):
	print("\nRunning...")
	# inputFolder outputFolder, appNumber
	getSource(argv[0], argv[1], int(argv[2]))

if __name__== "__main__":
	main(sys.argv[1:])