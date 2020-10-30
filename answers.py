import random


def get_question_answers(d):

    # added all answers to the answers list
    # so i can iterate over them for the
    # trivia questions
    answers = []
    answers.append(d['correct'])
    for answer in d['incorrect']:
        answers.append(answer)

    # don't want the answers coming out the
    # same every time! that's no fun!
    # imported random up top
    random.shuffle(answers)
    return answers
