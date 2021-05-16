import unittest
from unittest.mock import patch
import wordCount

class testCase_palindrome(unittest.TestCase):
    #Testing if userinput is a string of numbers
    numberInput = '1 2 3 4 5 6 7 8 9 10'
    @patch('builtins.input', return_value = numberInput)
    def test_string_of_ints(self, mock_input):
        result = wordCount.wordCounter()
        self.assertEqual(result, 10)

    #Testing multiple spaces in the sentence
    manySpacesInput = 'hello this is me        inputting      many spaces      in the      sentence     '
    @patch('builtins.input', return_value = manySpacesInput)
    def test_string_with_multiple_spaces(self, mock_input):
        result = wordCount.wordCounter()
        self.assertEqual(result, 10)

    #Testing with special characters
    specialInput = '^$&*@^! &@!$^@!&*$^ !@&$@!&$^!@& $!@&$!@#*()!@#* &*( @#*())'
    @patch('builtins.input', return_value = specialInput)
    def test_special_chars(self, mock_input):
        result = wordCount.wordCounter()
        self.assertEqual(result, 6)

    #Testing with special characters and uppercase/lower case letters
    specialInput2 = 'h311o mY n@m3 is jon@+|-|@n'
    @patch('builtins.input', return_value = specialInput2)
    def test_special_chars_complex(self, mock_input):
        result = wordCount.wordCounter()
        self.assertEqual(result, 5)

    # Testing with one long word
    oneInput = 'sjiofidfauaisdfuaidasfASDASDSDASDSDsdofuaisdfuasdklfjasdfASHDKASJDH*@jklkasdj90872329023rq2038'
    @patch('builtins.input', return_value = oneInput)
    def test_one_word(self, mock_input):
        result = wordCount.wordCounter()
        self.assertEqual(result, 1)

    # Testing with no input
    noInput = ''
    @patch('builtins.input', return_value = noInput)
    def test_no_words(self, mock_input):
        result = wordCount.wordCounter()
        self.assertEqual(result, 0)



if __name__ == '__main__':
    unittest.main()
