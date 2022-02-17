# pylint: disable=missing-docstring

import unittest

from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_anna_is_a_palindrome(self):
        self.assertIs(is_palindrome("anna"), True)

    def test_walter_is_not_a_palindrome(self):
        self.assertIs(is_palindrome("walter"), False)
        
    def test_anla_is_not_a_palindrome(self):
        self.assertIs(is_palindrome("anla"), False)
   
    def test_annb_is_not_a_palindrome(self):
        self.assertIs(is_palindrome("annb"), False)

    def test_rats_live_on_no_evil_star_is_not_a_palindrome(self):
        self.assertIs(is_palindrome("Rats live on no evil star"), True)

if __name__ == '__main__':
    unittest.main()
