def main():
    # Get user input and convert it to lower case.
    userInput = input("Enter your string to test for palindrome: ").lower()

    cleanedString = ''

    # Loop through user string and remove all the spaces in it
    for char in userInput:
        if char != ' ':
            cleanedString += char

    # Convert string into list to compare
    stringList = list(cleanedString)

    isPalindrome = checkPalindrome(stringList)

    if isPalindrome == False:
        print("Your string is not a palindrome")
    else:
        print("Your string is a palindrome")

def palindromeChecker(stringList):
    # Get and store length fo stringList
    stringLen = len(stringList)

    # Copy list and reverse it
    reverseString = stringList.copy()
    reverseString.reverse()

    # Check to see if the reverse list and string list have the same characters in the same order
    # Meaning check if the string is read the same forward and backwards
    for i in range(stringLen):
        if(stringList[i] != reverseString[i]):
            return False
    return True

if __name__ == "__main__":
    main()
