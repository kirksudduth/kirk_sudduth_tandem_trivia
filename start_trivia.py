import json
import random


def start_trivia():
    with open("data.json") as json_file:
        data = json.load(json_file)
        user_choice = ""
        for d in data:

            # added all answers to the answers list
            # so i can iterate over them for the
            # trivia questions
            answers = []
            answers.append(d['correct'])
            for incorrect in d['incorrect']:
                answers.append(incorrect)
            print(d['question'])
            random.shuffle(answers)
            for index, a in enumerate(answers):
                print(f'{index + 1}. {a}')
            choice = input(">> ")

            if choice == '1':
                if answers[0] == d['correct']:
                    print("\n\n*** CORRECT ***\n\n")
                else:
                    print("\n\n*** INCORRECT ***\n")
                    print(d['correct'], 'is the right answer.\n\n')

            if choice == '2':
                if answers[1] == d['correct']:
                    print("\n\n*** CORRECT ***\n\n")
                else:
                    print("\n\n*** INCORRECT ***\n")
                    print(d['correct'], 'is the right answer.\n\n')

            if choice == '3':
                if answers[2] == d['correct']:
                    print("\n\n*** CORRECT ***\n\n")
                else:
                    print("\n\n*** INCORRECT ***\n")
                    print(d['correct'], 'is the right answer.\n\n')

            if choice == '4':
                if answers[3] == d['correct']:
                    print("\n\n*** CORRECT ***\n\n")
                else:
                    print("\n\n*** INCORRECT ***\n")
                    print(d['correct'], 'is the right answer.\n\n')
