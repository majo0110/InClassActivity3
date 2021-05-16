from io import StringIO
import palindrome

# Code was based off of the tutorial
# https://www.linuxjournal.com/content/testing-your-code-pythons-pytest-part-ii

# Testing if user input is a string of numbers
numberInput = StringIO("1234554321\n")
def test_string_of_numbers(monkeypatch):
    monkeypatch.setattr('sys.stdin', numberInput)
    assert palindrome.palindromeChecker() == True

# Testing for input that includes special characters and spaces
# It is a palindrome
specialInput = StringIO(")(*&^% %^&*()\n")
def test_special_chars(monkeypatch):
    monkeypatch.setattr('sys.stdin', specialInput)
    assert palindrome.palindromeChecker() == True

# Testing for input that includes special characters and spaces
# It isn't a palindrome
specialInput2 = StringIO("!@$%!@*()#$ @!()$*@!(*$(!@)$)\n")
def test_special_chars2(monkeypatch):
    monkeypatch.setattr('sys.stdin', specialInput2)
    assert palindrome.palindromeChecker() == False

#Testing normal string with spaces that is a palindrome
stringInput = StringIO("Mr Owl ate my metal worm\n")
def test_normal_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', stringInput)
    assert palindrome.palindromeChecker() == True

#Testing normal string with spaces that isn't a palindrome
stringInput2 = StringIO("I am writing something random to fill in input\n")
def test_normal_input2(monkeypatch):
    monkeypatch.setattr('sys.stdin', stringInput2)
    assert palindrome.palindromeChecker() == False

#Complex test case using special chars, numbers, and mix of lower/uppercase. Not palindrome
complexInput = StringIO("Y0u uu0n+ uNdER$+@n|) +|-|iS\n")
def test_complex(monkeypatch):
    monkeypatch.setattr('sys.stdin', complexInput)
    assert palindrome.palindromeChecker() == False

#Complex test case using special chars, numbers, and mix of lower/uppercase. Is a palindrome
complexInput2 = StringIO("R@N|)0M words will Be hERE LOL EREH Eb lliW sdrow M0)|N@R \n")
def test_complex2(monkeypatch):
    monkeypatch.setattr('sys.stdin', complexInput2)
    assert palindrome.palindromeChecker() == True

# Test input of one worded palindrome. Is a palindrome
simpleWord = StringIO("madammadam")
def test_simple(monkeypatch):
    monkeypatch.setattr('sys.stdin', simpleWord)
    assert palindrome.palindromeChecker() == True

# Test input of one worded palindrome. Isn't a palindrome
simpleWord2 = StringIO("jonathanwashereheheheheh")
def test_simple2(monkeypatch):
    monkeypatch.setattr('sys.stdin', simpleWord2)
    assert palindrome.palindromeChecker() == False
