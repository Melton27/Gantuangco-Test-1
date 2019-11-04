import csv
import json
import sys
from os import path

Csvfile = sys.argv[1]
Jsonfile = sys.argv[2]

if Csvfile.endswith(".csv") and path.exists(Csvfile):
  if not  Jsonfile.endswith(".json"):
    Jsonfile += ".json"

data = {}

with open(Csvfile, "r") as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows["Name"]
        data[id] = rows

with open(Jsonfile, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent=4)) 
    print("Success!")       

check = sys.argv[3]

import pathlib
check = pathlib.Path(Jsonfile)
if check.exists ():
    print ("File exist")
else:
    print ("File not exist")


  
