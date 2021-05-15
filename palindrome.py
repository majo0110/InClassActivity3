def main():
    # Get user input and convert it to lower case.
    userInput = input("Enter your word to test for palindrome: ").lower()

    cleanedString = ''

    for char in userInput:
        if char != ' ':
            cleanedString += char

    print(cleanedString)

if __name__ == "__main__":
    main()
