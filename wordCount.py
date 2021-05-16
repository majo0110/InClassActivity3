def main():
    print(wordCounter())

def wordCounter():
    # Get user input and split it into a list
    userInput = input("Enter your word to sentence to see word count: ")
    splitInput = userInput.split()

    # Return the length of list
    return(len(splitInput))

if __name__ == "__main__":
    main()
