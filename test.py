import unittest
from answers import get_question_answers


class GetQuestionAnswers(unittest.TestCase):

    def test_get_answers(self):
        data = {}
        data['correct'] = "Yes"
        data['incorrect'] = ["Not Exactly", "Eeeehh", "Nope"]

        result = len(get_question_answers(data))

        self.assertEqual(
            result, (len(data['incorrect']) + 1))


if __name__ == "__main__":
    unittest.main()
