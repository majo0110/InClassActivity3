import unittest
from unittest.mock import patch
import palindrome

class testCase_palindrome(unittest.TestCase):
    #Testing if userinput are numbers
    numberInput = '123321'
    @patch('builtins.input', return_value = numberInput)
    def test_string_of_ints(self, mock_input):
        result = palindrome.palindromeChecker()
        self.assertEqual(result, True)

    #Inputting a integer as the userInput
    intInput = 123321
    @patch('builtins.input', return_value = numberInput)
    def test_ints(self, mock_input):
        self.assertRaises(TypeError, palindrome.palindromeChecker())

    #Testing for inputs that include special characters and spaces
    # Is a palindrome
    specialInput = '!@#$% %$#@!'
    @patch('builtins.input', return_value = specialInput)
    def test_special_chars(self, mock_input):
        result = palindrome.palindromeChecker()
        self.assertEqual(result, True)

    # Isn't a palindrome
    specialInput2 = '() *& ()'
    @patch('builtins.input', return_value = specialInput2)
    def test_special_chars2(self, mock_input):
        result = palindrome.palindromeChecker()
        self.assertEqual(result, False)

    #Testing normal string with spaces that is a palindrome
    stringInput = "racecar"
    @patch('builtins.input', return_value = stringInput)
    def test_string_true(self, mock_input):
        result = palindrome.palindromeChecker()
        self.assertEqual(result, True)

    #Testing normal string with spaces that is not a palindrome
    stringInput = "your test case is not a palindrome"
    @patch('builtins.input', return_value = stringInput)
    def test_string_false(self, mock_input):
        result = palindrome.palindromeChecker()
        self.assertEqual(result, False)



if __name__ == '__main__':
    unittest.main()
