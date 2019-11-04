import csv
import json

csvfile = "demo.csv"
jsonfile = "demo.json"

data = {}

with open(csvfile, "r") as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows ["Name"]
        data[id] = rows
    
with open(jsonfile, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))

