import csv
import json
import sys
import argparse
import os.path
from os import path
import getopt

csvfile = "demo.csv"
jsonfile = "Sample.json"


data = {}

with open(csvfile, "r") as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows["Name"]
        data[id] = rows

with open(jsonfile, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent=4)) 
    print("Success!")       

import pathlib
file = pathlib.Path("Sample.json")
if file.exists ():
    print ("File exist")
else:
    print ("File not exist")

parser = argparse.ArgumentParser(description='AGPARSE!')
parser.add_argument("--a")

args = parser.parse_args()
a = args.a
print(a)

#ef main(argv):
  # inputfile = 'Sample.csv'
  # outputfile = 'Sample.json'
  # try:
#   opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  # except getopt.GetoptError:
#print('Assessment.py -i <Sample.csv> -o <Sample.json>')
  #    sys.exit(2)
  # for opt, arg in opts:
#if opt == '-h':
#    sys.exit()
    #  elif opt in ("-i", "--ifile"):
    #     inputfile = arg
#elif opt in ("-o", "--ofile"):
       #  outputfile = arg
#print ('Input file is "', inputfile)
 #  print ('Output file is "', outputfile)

#if __name__ == "__main__":
  # main(sys.argv[1:])

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

