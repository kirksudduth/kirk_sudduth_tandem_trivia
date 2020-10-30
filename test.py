import unittest
from answers import get_question_answers, show_answers


class Answers(unittest.TestCase):

    def test_get_answers(self):
        data = {}
        data['correct'] = "Yes"
        data['incorrect'] = ["Not Exactly", "Eeeehh", "Nope"]

        # test to make sure the answers are getting added to
        # the answers list correctly
        result = len(get_question_answers(data))

        self.assertEqual(
            result, (len(data['incorrect']) + 1))

    def test_get_answers_diff_values(self):
        data = {}
        data['correct'] = 8
        data['incorrect'] = [12, 5, None, "hahah"]

        # test checking that different values don't change
        # the outcome of my get_question_answers function
        result = len(get_question_answers(data))

        self.assertEqual(result, (len(data['incorrect']) + 1))

    # *** WIP ***
    # def test_return_answers(self):
    #     answers = ["East", "West", "North", "South"]
    #     result = show_answers(answers)


if __name__ == "__main__":
    unittest.main()
