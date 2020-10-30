import json
import time
import random
import os


def questions_list():
    os.system('cls' if os.name == 'nt' else 'clear')
    with open("data.json") as json_file:
        data = json.load(json_file)
        random.shuffle(data)
        for d in data:
            question = d['question']
            print(f'\n{question}')
            time.sleep(1)

        input("\n\nPress Enter to return to main menu.\n\n")
