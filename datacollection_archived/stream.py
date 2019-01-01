"""

To run this, adjust time zone to UTC

COMMANDS:
source activate thesis
python stream.py queries.csv

"""

import sys
from datetime import datetime
from tools import stream_tools as stream
from tools import credentials as cred

def run(queryFile):

    #Create Query list
    queries = ""
    with open(queryFile) as i_file:
        queries = i_file.read()
    queries_list = queries.split(",")

    # choose which Twitter app to use for this query
    i = 1

    print('Streaming for ' + queryFile)

    auth = cred.getAuth(i, "user")
    now = datetime.now()
    out_Path = "data/" + now.strftime("%Y-%m-%d-%H-%M") + "-stream"

    stream.stream_tweets(auth, queries_list, out_Path)


def main(argv):
  print("Running stream.py")
  run(argv[0])
  
if __name__== "__main__":
  main(sys.argv[1:])