import unittest
from trivia import func1, func2


class TestTrivia(unittest.TestCase):
    def test_func1(self):
        self.assertEqual(func1(1), 0)

    def test_func2(self):
        self.assertEqual(func2(2,1), 3)
        self.assertEqual(func2(2.1, 1.2), 3.3)

if __name__ == '__main__':
    unittest.main()

