from io import StringIO
import wordCount

# Code was based off of the tutorial
# https://www.linuxjournal.com/content/testing-your-code-pythons-pytest-part-ii

# Testing if user input is a string of numbers
numberInput = StringIO('1 2 3 4 5 6 7 8 9 10\n')
def test_string_of_numbers(monkeypatch):
    monkeypatch.setattr('sys.stdin', numberInput)
    assert wordCount.wordCounter() == 10

# Testing multiple spaces in the sentence
multipleSpaces = StringIO('This    is     a sentence with        multiple    spaces       inbetween words\n')
def test_many_spaces(monkeypatch):
    monkeypatch.setattr('sys.stdin', multipleSpaces)
    assert wordCount.wordCounter() == 9

# Testing special characters
specialCharInput = StringIO("$@&*!$*@ !$*@!&$*@!$*&@ !$* @&!*$@!& $*(@!& $*(@!$&*@(!$ &@!*($&@))))\n")
def test_special(monkeypatch):
    monkeypatch.setattr('sys.stdin', specialCharInput)
    assert wordCount.wordCounter() == 7

# Testing special characters with upper and lower case letter
specialCharInput2 = StringIO("D*&*&* asdhad&*&*ADS &SH*hhdasda8** K*&BSA@\n")
def test_special2(monkeypatch):
    monkeypatch.setattr('sys.stdin', specialCharInput2)
    assert wordCount.wordCounter() == 4

# Testing with one long word
oneWordInput = StringIO("hellomynameisjonathanandimtestingthiswithoneword")
def test_one_word(monkeypatch):
    monkeypatch.setattr('sys.stdin', oneWordInput)
    assert wordCount.wordCounter() == 1

# Testing with empty input
noInput = StringIO("\n")
def test_no_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', noInput)
    assert wordCount.wordCounter() == 0
