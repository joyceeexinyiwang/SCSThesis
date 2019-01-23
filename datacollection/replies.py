"""
python replies.py ids_file inputFolder outputFolder loops



"""

import sys, json, os

def replies(IDs, inputFolder, outputFolder, loops):
	fileCount = 0
	path = outputFolder + "/replies"
	f = open(path + "_" + str(fileCount) + ".json", 'a+',encoding='utf8')
	count = 0
	maxTweets = 10000

	for i in range(loops):
		for (dirpath, dirnames, filenames) in os.walk(inputFolder):
			for filename in filenames:
				if filename.endswith('.json'): 
					with open(dirpath+"/"+filename) as infile:
						for line in infile:
							t = json.loads(line)
							if t["id"] not in IDs:
								print(t["id"])
								if t["in_reply_to_status_id"] in IDs:
									IDs.add(t["id"])
									f.write(line)
									count += 1
								elif "quoted_status" in t and t["quoted_status"]["id"] in IDs:
									IDs.add(t["id"])
									f.write(line)
									count += 1
								if count >= maxTweets:
									count = 0
									fileCount += 1
									f.close()
									f = open(path + "_" + str(fileCount) + ".json", 'a+',encoding='utf8')

def main(argv):
	print("\nRunning...")
	# ids_file inputFolder outputFolder loops

	ids = []
	idStr = ""
	with open(argv[0]) as i_file:
		idStr = i_file.read()
	ids = idStr.split(",")

	replies(ids, argv[1], argv[2], int(argv[3]))

if __name__== "__main__":
	main(sys.argv[1:])

# filter big file for replies
# while loop:
# 	filter big file again to check for replies of replies