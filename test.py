import unittest
import sys
from io import StringIO
from unittest.mock import patch
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

    def test_answers_stdout(self):
        answers = ["East", "West", "North", "South"]

        # my understanding of this code is that it creates an
        # instance of a stringIO object by using patch as a
        # context manager -- sys.stdout is the target argument
        # and new=StringIO is the kind of file object that's being
        # created for the test
        with patch('sys.stdout', new=StringIO()) as fake_out:
            # the result of show_answers(answers) is added to the fake_out
            # object as the value property
            show_answers(answers)
            expected = "1. East\n2. West\n3. North\n4. South\n"
            # fake_out.getvalue() is the value of show_answers(answers)
            self.assertEqual(fake_out.getvalue(),
                             expected)


if __name__ == "__main__":
    unittest.main()
