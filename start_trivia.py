import json


with open("data.json") as json_file:
    data = json.load(json_file)
    for d in data:
        print(d['question'])
