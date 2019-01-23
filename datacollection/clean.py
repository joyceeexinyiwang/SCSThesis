"""

python clean.py dedup inputFolder outputFileName
python clean.py filterByTweet queries.csv inputFolder outFolder

"""
import json, sys, os
from tools import basics
from tools import general_tools as gen

def main(argv):
	print("")
	if argv[0] == "dedup":
		# inputFolder outputFileName
		basics.dedup(argv[1], argv[1]+"/clean", argv[2])

	elif argv[0] == "date":
		pass
		
	elif argv[0] == "filterByTweet":
		query = argv[1]
		inputFolder = argv[2]
		outFolder = argv[3]
		tweets = {}
		with open(query) as f:
			for line in f:
				line = line.strip().split(",")
				tweets[int(line[0])] = []

		fs = {}
		if not os.path.exists(outFolder):
			os.makedirs(outFolder)
		for idN in tweets:
			fs[idN] = open(outFolder + "/" + str(idN) + ".txt", "w")

		for (dirpath, dirnames, filenames) in os.walk(inputFolder):
			for filename in filenames:
				if filename.endswith('.json'): 
					print("Currently on " + filename)
					with open(dirpath+"/"+filename) as f:
						for line in f:
							for idN in tweets:
								relation = gen.getRelation(line, idN)
								if relation != None:
									tweets[idN].append(line)
									fs[idN].write(line)
		for idN in tweets:
			ts = tweets[idN]
			basics.writeFile(outFolder, str(idN), ts)

		for f in fs:
			f.close()

if __name__== "__main__":
	main(sys.argv[1:])