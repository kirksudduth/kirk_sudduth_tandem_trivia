import json


def questions_list():
    with open("data.json") as json_file:
        data = json.load(json_file)
        for d in data:
            question = d['question']
            print(f'\n{question}')

        input("Press Enter to return to main menu.\n\n")
