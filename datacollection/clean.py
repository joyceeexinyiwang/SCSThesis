"""

python clean.py dedup inputFolder outputFolder filename
python clean.py filterByTweet queries.csv inputFolder outFolder
python clean.py dedup_and_separate inputFolder outputFolder filename

example:
python clean.py dedup_and_separate /Volumes/JoyceXYW/Joyce/Thesis/data_accum/Spring/AJEnglish /Volumes/JoyceXYW/Joyce/Thesis/_working AJEnglish_deduped
python clean.py dedup_and_separate /Volumes/JoyceXYW/Joyce/Thesis/data_accum/Spring/washingtonpost /Volumes/JoyceXYW/Joyce/Thesis/_working washingtonpost_deduped
python clean.py dedup_and_separate /Volumes/JoyceXYW/Joyce/Thesis/data_accum/Spring/WSJ /Volumes/JoyceXYW/Joyce/Thesis/_working WSJ_deduped
python clean.py dedup_and_separate /Volumes/JoyceXYW/Joyce/Thesis/data_accum/Spring/nytimes /Volumes/JoyceXYW/Joyce/Thesis/_working nytimes_deduped
python clean.py dedup_and_separate /Volumes/JoyceXYW/Joyce/Thesis/data_accum/Spring/ChinaDaily /Volumes/JoyceXYW/Joyce/Thesis/_working ChinaDaily_deduped
python clean.py dedup_and_separate /Volumes/JoyceXYW/Joyce/Thesis/data_accum/Spring/NBCNews /Volumes/JoyceXYW/Joyce/Thesis/_working NBCNews_deduped



REMEMBER:
change the parameters for "basics.dedup_and_separate(...)" (replace keyword like "#AJOpinion")

"""
import json, sys, os
from tools import basics
from tools import general_tools as gen

def main(argv):
	print("")

	if argv[0] == "dedup_and_separate":
		print(argv)
		basics.dedup_and_separate(argv[1], argv[2], argv[3] , "Opinion")

	elif argv[0] == "dedup":
		# inputFolder outputFolder
		basics.dedup(argv[1], argv[2] + "/NEW_DEDUPED", argv[3])

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