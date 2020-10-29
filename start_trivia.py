import json
import random


def start_trivia():
    score = 0
    with open("data.json") as json_file:
        data = json.load(json_file)
        for d in data:
            print(d['question'])

            # added all answers to the answers list
            # so i can iterate over them for the
            # trivia questions

            answers = []
            answers.append(d['correct'])
            for incorrect in d['incorrect']:
                answers.append(incorrect)

            # don't want the answers coming out the
            # same every time! that's no fun!
            # imported random up top

            random.shuffle(answers)

            # used the enumerate function with index so
            # i can number answers for user input

            for index, a in enumerate(answers):
                print(f'{index + 1}. {a}')

            # take the index of the chosen answer from answers list
            # and check against the correct answer which is
            # a property of 'd'

            # *** if choice == int(f'{index + 1}') ***
            # !!! what if more than 4 answers?? !!!
            while True:
                try:
                    choice = int(input("\n>> "))
                    assert 0 < choice <= len(answers)
                except ValueError:
                    print("Please enter an integer.")
                except AssertionError:
                    print(
                        f'Please enter an integer between 1 and {len(answers)}')
                else:
                    break

            if choice == 1:
                if answers[0] == d['correct']:
                    print("\n\n*** CORRECT ***\n\n")
                    score += 1
                else:
                    print("\n\n*** INCORRECT ***\n")
                    print(d['correct'], 'is the right answer.\n\n')

            if choice == 2:
                if answers[1] == d['correct']:
                    print("\n\n*** CORRECT ***\n\n")
                    score += 1
                else:
                    print("\n\n*** INCORRECT ***\n")
                    print(d['correct'], 'is the right answer.\n\n')

            if choice == 3:
                if answers[2] == d['correct']:
                    print("\n\n*** CORRECT ***\n\n")
                    score += 1
                else:
                    print("\n\n*** INCORRECT ***\n")
                    print(d['correct'], 'is the right answer.\n\n')

            if choice == 4:
                if answers[3] == d['correct']:
                    print("\n\n*** CORRECT ***\n\n")
                    score += 1
                else:
                    print("\n\n*** INCORRECT ***\n")
                    print(d['correct'], 'is the right answer.\n\n')

    print(score)
