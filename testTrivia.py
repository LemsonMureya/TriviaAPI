import unittest
from trivia import func1, func2, get_category, get_difficulty, get_questions


class TestTrivia(unittest.TestCase):
    # def test_func1(self):
    #     self.assertEqual(func1(1), 0)

    # def test_func2(self):
    #     self.assertEqual(func2(2,1), 3)
    #     self.assertEqual(func2(2.1, 1.2), 3.3)

    #assertEqual -> to check for an expected result
    #assertTrue -> to verify a condition
    #assertFalse -> to verify a condition
    #assertRaises -> to verify that a specific exception gets raised 
    def get_category():
        self.assertEqual(get_category(), 'geography')
        self.assertEqual(get_category(), 'history')
        
    def get_difficulty():
        self.assertEqual(get_difficulty(), 'easy')
        self.assertEqual(get_difficulty(), 'medium')

    def get_questions():
        self.assertEqual(get_questions(), 2)
        self.assertEqual(get_questions(), '4')

    # def make_database(data):
    #     pass

    # def update_database(data):
    #     pass
    # def revisit():
    #     pass


if __name__ == '__main__':
    unittest.main()

