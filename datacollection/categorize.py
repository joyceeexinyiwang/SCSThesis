"""

python categorize.py inputFolder outputFolder

categorize into reply/retweet/quote 

"""

import sys, datetime, os, json
from tools import general_tools as gen

def categorize(inputFolder, outputFolder):

	if not os.path.exists(outputFolder + "/NEW/"):
		os.makedirs(outputFolder + "/NEW/")

	for (dirpath, dirnames, filenames) in os.walk(inputFolder):
		for filename in filenames:
			if filename.endswith('.json'): 
				print("Currently on " + filename)
				with open(dirpath+"/"+filename) as i_file:

					f_ret = open(outputFolder + "/NEW/" + filename+ "_retweets.json", "w")
					f_rep = open(outputFolder + "/NEW/" + filename+ "_replies.json", "w")
					f_quo = open(outputFolder + "/NEW/" + filename+ "_quotes.json", "w")

					for line in i_file:
						relation = gen.getRelationNoID(line)
						if relation == "retweet":
							f_ret.write(line)
						elif relation == "reply":
							f_rep.write(line)
						elif relation == "quote":
							f_quo.write(line)

					f_ret.close()
					f_rep.close()
					f_quo.close()

def main(argv):
	print("\nRunning...")
	# inputFolder outputFolder
	categorize(argv[0], argv[1])

if __name__== "__main__":
	main(sys.argv[1:])