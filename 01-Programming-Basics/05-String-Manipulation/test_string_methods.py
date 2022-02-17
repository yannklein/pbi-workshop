# pylint: disable=missing-docstring

import unittest

from string_methods import add_comma
from string_methods import belongs_to
from string_methods import count_repetition
from string_methods import is_a_question
from string_methods import replace
from string_methods import remove_surrounding_whitespaces
from string_methods import full_description_concatenation
from string_methods import full_description_formatting

class TestStringMethods(unittest.TestCase):
    # add_comma

    def test_strings_boris_romain_seb(self):
        self.assertEqual(add_comma("boris romain seb"), "boris, romain, seb")

    def test_strings_boris_seb_romain(self):
        self.assertEqual(add_comma("boris seb romain"), "boris, seb, romain")


    # belongs_to

    def test_include_word(self):
        self.assertEqual(belongs_to("hey jude", "jude"), True)

    def test_do_not_include_word(self):
        self.assertEqual(belongs_to("hey jude", "joe"), False)


    # count_repetition

    def test_numbers_0_0_1_2_0_on_0(self):
        self.assertEqual(count_repetition("00120", "0"), 3)

    def test_numbers_0_0_1_2_0_on_3(self):
        self.assertEqual(count_repetition("00120", "3"), 0)


    # is_a_question

    def test_is_a_question(self):
        self.assertEqual(is_a_question("How are you?"), True)

    def test_is_not_a_question(self):
        self.assertEqual(is_a_question("Fine."), False)


    #delete_surrounding_whitespaces

    def test_leading_whitespaces(self):
        self.assertEqual(remove_surrounding_whitespaces("  hey yo"), "hey yo")

    def test_trailing_whitespaces(self):
        self.assertEqual(remove_surrounding_whitespaces("hey yo  "), "hey yo")

    def test_whitespaces(self):
        self.assertEqual(remove_surrounding_whitespaces(" hey yo  "), "hey yo")


    # replace

    def test_casanova_to_cosonovo(self):
        self.assertEqual(replace("casanova", "a", "o"), "cosonovo")

    def test_kosovo_to_kasava(self):
        self.assertEqual(replace("kosovo", "o", "a"), "kasava")


    # full_description_concatenation

    def test_john_doe_33_concatenation(self):
        self.assertEqual(full_description_concatenation("John", "Doe", 33), "John Doe is 33")


    # full_description_formatting

    def test_john_doe_33_formatting(self):
        self.assertEqual(full_description_formatting("John", "Doe", 33), "John Doe is 33")

if __name__ == '__main__':
    unittest.main()
