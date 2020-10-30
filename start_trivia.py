import json
import random
import os
import time


def start_trivia():
    score = 0
    with open("data.json") as json_file:
        data = json.load(json_file)

        # don't want users questions to be the same
        # every time
        random.shuffle(data)

        # only getting the first 10 items in the shuffled
        # data list because we only want a 10 question quiz
        #  --- --- --- --- --- --- --- --- --- --- ---
        # [:10] implies that start at 0 index to 9 index
        for d in data[:10]:
            os.system('cls' if os.name == 'nt' else 'clear')
            question = d['question']
            print(f'[?] {question}')

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
                    print("\n\n*~*~*~*~*~*~*~*~*~*~*")
                    print("*~* :) CORRECT (: *~*")
                    print("*~*~*~*~*~*~*~*~*~*~*\n\n")
                    score += 1
                    time.sleep(.5)
                else:
                    print("\n\n*?*?*?*?*?*?*?*?*?*?*?*")
                    print("*?* :( INCORRECT ): *?*")
                    print("*?*?*?*?*?*?*?*?*?*?*?*\n")
                    print(d['correct'], 'is the right answer.\n\n')
                    time.sleep(1)

            if choice == 2:
                if answers[1] == d['correct']:
                    print("\n\n*~*~*~*~*~*~*~*~*~*~*")
                    print("*~* :) CORRECT (: *~*")
                    print("*~*~*~*~*~*~*~*~*~*~*\n\n")
                    score += 1
                    time.sleep(.5)
                else:
                    print("\n\n*?*?*?*?*?*?*?*?*?*?*?*")
                    print("*?* :( INCORRECT ): *?*")
                    print("*?*?*?*?*?*?*?*?*?*?*?*\n")
                    print(d['correct'], 'is the right answer.\n\n')
                    time.sleep(1)

            if choice == 3:
                if answers[2] == d['correct']:
                    print("\n\n*~*~*~*~*~*~*~*~*~*~*")
                    print("*~* :) CORRECT (: *~*")
                    print("*~*~*~*~*~*~*~*~*~*~*\n\n")
                    score += 1
                    time.sleep(.5)
                else:
                    print("\n\n*?*?*?*?*?*?*?*?*?*?*?*")
                    print("*?* :( INCORRECT ): *?*")
                    print("*?*?*?*?*?*?*?*?*?*?*?*\n")
                    print(d['correct'], 'is the right answer.\n\n')
                    time.sleep(1)

            if choice == 4:
                if answers[3] == d['correct']:
                    print("\n\n*~*~*~*~*~*~*~*~*~*~*")
                    print("*~* :) CORRECT (: *~*")
                    print("*~*~*~*~*~*~*~*~*~*~*\n\n")
                    score += 1
                    time.sleep(.5)
                else:
                    print("\n\n*?*?*?*?*?*?*?*?*?*?*?*")
                    print("*?* :( INCORRECT ): *?*")
                    print("*?*?*?*?*?*?*?*?*?*?*?*\n")
                    print(d['correct'], 'is the right answer.\n\n')
                    time.sleep(1)
    if score == 10:
        print(
            f'WHOA. {score}/10\nU SMORT...\nRather, you know all these trivia questions. WAY TO GO!!\n')
        input("Press Enter to return to main menu.")
    if score == 9:
        print(
            f'You did great! {score}/10\nAlmost got them all correct.\nPersistence pays interest.\n')
        input("Press Enter to return to main menu.")
    if 6 < score < 9:
        print(
            f'These aren\'t things everyone knows, obviously. ¯\_(ツ)_/¯\nTry again to score higher than {score}/10\n')
        input("Press Enter to return to main menu.")
    if score < 7:
        print(
            f'Play again?\n{score}/10 is an unacceptable score for someone so smart ಠ_ಠ\n')
        input("Press Enter to return to main menu.")
