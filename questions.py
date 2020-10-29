import json
import time


def questions_list():
    with open("data.json") as json_file:
        data = json.load(json_file)
        for d in data:
            question = d['question']
            print(f'\n{question}')
            time.sleep(1.5)

        input("\n\nPress Enter to return to main menu.\n\n")
