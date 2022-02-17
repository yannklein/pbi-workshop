import unittest
from find_middle_string import find_middle_string, get_middle_value, get_size_of_string


class TestFindMiddleString(unittest.TestCase):
    def test_get_size_of_string(self):
        self.assertEqual(get_size_of_string("hello"), 5)
        self.assertEqual(get_size_of_string("allo"), 4)
        self.assertEqual(get_size_of_string("bonjour"), 7)

    def test_get_middle_value(self):
        self.assertEqual(get_middle_value(1, 2, 3), 2)
        self.assertEqual(get_middle_value(3, 2, 1), 2)
        self.assertEqual(get_middle_value(2, 1, 3), 2)
        self.assertEqual(get_middle_value(3, 1, 2), 2)
        self.assertEqual(get_middle_value(1, 3, 2), 2)
        self.assertEqual(get_middle_value(2, 3, 1), 2)
        self.assertEqual(get_middle_value(1, 3, 3), -1)

    def test_find_middle_string(self):
        self.assertEqual(find_middle_string("hello", "allo", "bonjour"), "hello")
        self.assertEqual(find_middle_string("allo", "hello", "bonjour"), "hello")
        self.assertEqual(find_middle_string("allo", "bonjour", "hello"), "hello")
        self.assertEqual(find_middle_string("allo", "bonjour", "helo"), "two or more strings have the same length")


if __name__ == '__main__':
    unittest.main()
