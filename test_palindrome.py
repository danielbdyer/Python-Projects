import unittest
from palindrome import Palindrome

class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.palindrome = Palindrome()

    def test_comparing_reversed_string_of_known_palindrome(self):
        self.assertEqual(self.palindrome.isPalindrome("deleveled"),"deleveled")

    def test_comparing_reversed_string_of_nonpalindrome(self):
        self.assertNotEqual(self.palindrome.isPalindrome("sentences"),"sentences")

unittest.main(verbosity=2)

# UNIT TESTS FOR THE PALINDROME FUNCTION
# [one test for true palindrome, one test for false]
# Checks against a known palindrome / a non-palindrome

# Given:	A palindrome or non-palindrome
# When:	    Reversed and compared to its original
# Then:	    I should be able to get a True/False from comparison 
