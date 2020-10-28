import json
import random

with open("data.json") as json_file:
    data = json.load(json_file)
    for d in data:
        answers = []
        answers.append(d['correct'])
        for incorrect in d['incorrect']:
            answers.append(incorrect)
        print(d['question'])
        random.shuffle(answers)
        for a in answers:
            print("answer: ", a)
