from tools import general_tools
import json, sys


def main(argv):
  print("Running")
  general_tools.getTimeline("km")
  
if __name__== "__main__":
  main(sys.argv)