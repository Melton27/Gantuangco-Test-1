import csv, json

csvFilePath = "Sample.csv"
jsonFilePath = "Sample.json"

data = {}

with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows["Year"]
        data[id] = rows

with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))        