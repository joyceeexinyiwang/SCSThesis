"""

python stats.py inputFolder outputFolder

op stats:

python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/AJEnglish_deduped_separated/replies/opinion/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_opinion_getstats/AJEnglish_replies/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/ChinaDaily_deduped_separated/replies/opinion/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_opinion_getstats/ChinaDaily_replies/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/washingtonpost_deduped_separated/replies/opinion/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_opinion_getstats/washingtonpost_replies/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/WSJ_deduped_separated/replies/opinion/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_opinion_getstats/WSJ_replies/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/nytimes_deduped_separated/replies/opinion/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_opinion_getstats/nytimes_replies/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/NBCNews_deduped_separated/replies/opinion/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_opinion_getstats/NBCNews_replies/

python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/AJEnglish_deduped_separated/quotes/opinion /Volumes/JoyceXYW/Joyce/Thesis/_working/_opinion_getstats/AJEnglish_quotes/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/ChinaDaily_deduped_separated/quotes/opinion/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_opinion_getstats/ChinaDaily_quotes/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/washingtonpost_deduped_separated/quotes/opinion/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_opinion_getstats/washingtonpost_quotes/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/WSJ_deduped_separated/quotes/opinion/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_opinion_getstats/WSJ_quotes/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/nytimes_deduped_separated/quotes/opinion/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_opinion_getstats/nytimes_quotes/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/NBCNews_deduped_separated/quotes/opinion/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_opinion_getstats/NBCNews_quotes/

non op stats:

python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/AJEnglish_deduped_separated/replies/nonop/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_nonop_getstats/AJEnglish_replies/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/ChinaDaily_deduped_separated/replies/nonop/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_nonop_getstats/ChinaDaily_replies/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/washingtonpost_deduped_separated/replies/nonop/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_nonop_getstats/washingtonpost_replies/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/WSJ_deduped_separated/replies/nonop/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_nonop_getstats/WSJ_replies/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/nytimes_deduped_separated/replies/nonop/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_nonop_getstats/nytimes_replies/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/NBCNews_deduped_separated/replies/nonop/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_nonop_getstats/NBCNews_replies/

python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/AJEnglish_deduped_separated/quotes/nonop /Volumes/JoyceXYW/Joyce/Thesis/_working/_nonop_getstats/AJEnglish_quotes/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/ChinaDaily_deduped_separated/quotes/nonop/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_nonop_getstats/ChinaDaily_quotes/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/washingtonpost_deduped_separated/quotes/nonop/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_nonop_getstats/washingtonpost_quotes/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/WSJ_deduped_separated/quotes/nonop/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_nonop_getstats/WSJ_quotes/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/nytimes_deduped_separated/quotes/nonop/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_nonop_getstats/nytimes_quotes/
python stats.py /Volumes/JoyceXYW/Joyce/Thesis/_working/NBCNews_deduped_separated/quotes/nonop/ /Volumes/JoyceXYW/Joyce/Thesis/_working/_nonop_getstats/NBCNews_quotes/


"""

import sys, datetime, os, re, json, csv
import re
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def counts(inputFolder, outputFolder):

    if not os.path.exists(outputFolder + "/NEW/"):
        os.makedirs(outputFolder + "/NEW/")

    stats = open(outputFolder + "/NEW/"+ "stats.csv", 'w')
    f = csv.writer(stats, delimiter=',')
    f.writerow(["id_str", "full_text", "full_text_length", "cuss_n", "all_caps_n", "firstPP_n", "secondPP_n", "emoji_n", "VADER_pos", "VADER_compound", "VADER_neu", "VADER_neg",])

    cusswords = set()

    with open("cussWords.txt") as i_file:
        for w in i_file:
            cusswords.add(w.strip())

    # emojis = set()
    # with open("emojis.txt", encoding='utf-8') as i_file:
    #     for w in i_file:
    #         emojis.add(w.strip())

    secondPersonPronouns = set(["you","your","yours","yourself","yourselves"])
    firstPersonPronouns = set(["i","mine","we","us","our","ours","ourselves","me","my","mine"])

    analyzer = SentimentIntensityAnalyzer()

    totalN = 0
    cuss_n = 0
    all_caps_n = 0
    firstPP_n = 0
    secondPP_n = 0
    emoji_n = 0
    total_sentiments_score = 0

    for (dirpath, dirnames, filenames) in os.walk(inputFolder):
        for filename in filenames:
            if filename.endswith('.json'): 
                print("Currently on " + filename)
                with open(dirpath+"/"+filename) as i_file:

                    for line in i_file:
                        totalN += 1
                        tweet = json.loads(line)
                        full_text = tweet["full_text"]
                        full_text_length = len(full_text)
                        cleaned_tweet_list = (re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", full_text).split())

                        # check cuss words
                        cleaned_tweet_lowered = set([x.lower() for x in cleaned_tweet_list])
                        cuss = cleaned_tweet_lowered.intersection(cusswords)
                        if len(cuss) > 0: cuss_n += 1

                        # check second-person
                        firstPP = cleaned_tweet_lowered.intersection(firstPersonPronouns)
                        secondPP = cleaned_tweet_lowered.intersection(secondPersonPronouns)
                        if len(firstPP) > 0: firstPP_n += 1
                        if len(secondPP) > 0: secondPP_n += 1

                        # check all caps
                        all_caps = list(filter(lambda x: x.isupper(), cleaned_tweet_list))
                        if len(all_caps) > 0: all_caps_n += 1

                        # check emojis
                        emoji = re.findall(r'[\U0001f600-\U0001f64f]', full_text)
                        if len(emoji) > 0: emoji_n += 1

                        # get sentiment score
                        vs = analyzer.polarity_scores(full_text)
                        sentiment = vs["compound"]
                        # if analysis.sentiment.polarity > 0: 
                        #     sentiment = 'positive'
                        # elif analysis.sentiment.polarity == 0: 
                        #     sentiment = 'neutral'
                        # else: 
                        #     sentiment = 'negative'
                        total_sentiments_score += sentiment

                        f.writerow([tweet["id_str"], full_text, full_text_length, len(cuss), len(all_caps), len(firstPP), len(secondPP), ':'.join(str(item) for item in emoji), str(vs["pos"]), str(vs["compound"]), str(vs["neu"]), str(vs["neg"])])

    result = ""
    result+=("Stats:")
    result+=("\nTotal tweets: " + str(totalN))
    result+=("\n# of tweets with cusswords: " + str(cuss_n))
    result+=("\n# of tweets with all caps: " + str(all_caps_n))
    result+=("\n# of tweets with first-person pronouns: " + str(firstPP_n))
    result+=("\n# of tweets with second-person pronouns: " + str(secondPP_n))
    result+=("\n# of tweets with emojis:" + str(emoji_n))
    result+=("\naverage sentiments score (from -1 negative to 1 positive): " + str(total_sentiments_score/totalN))
    f = open(outputFolder + "/NEW/"+ "summary.txt", 'w')
    f.write(result)
    f.close()
    print(result)

def main(argv):
    print("\nRunning...")
    # lengths(argv[0])
    counts(argv[0], argv[1])
    # sourceInfo(argv[0], argv[1])

if __name__== "__main__":
    main(sys.argv[1:])