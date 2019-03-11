"""

python closelook.py inputFolder outputFolder

"""


import sys, datetime, os, re, json, csv

def closelook(inputFolder, outputFolder):

	if not os.path.exists(outputFolder + "/NEW/"):
		os.makedirs(outputFolder + "/NEW/")

	ids = set()

	for (dirpath, dirnames, filenames) in os.walk(inputFolder):
		for filename in filenames:
			if filename.endswith('.json'): 
				print("Currently on " + filename)
				with open(dirpath+"/"+filename) as f:

					f_write = open(outputFolder + "/NEW/" + filename[0:filename.index(".")]+ "_parsed.csv", "w")
					f_write.write("tweetID,in_reply_to_status_id_str\n")
					for line in f:
						tweet = json.loads(line)
						if tweet["id"] not in ids:
							f_write.write(str(tweet["id"]))
							f_write.write(",")
							f_write.write(str(tweet["in_reply_to_status_id_str"]))
							f_write.write("\n")
							ids.add(tweet["id"])
							# content = []
							# content.append(tweet["full_text"])
							# for u in tweet["entities"]["urls"]:
							# 	content.append(u["url"])
							# f_write.write("\t".join(content) + "\n")

					f_write.close()


def main(argv):
	closelook(argv[0], argv[1])

if __name__== "__main__":
	main(sys.argv[1:])
