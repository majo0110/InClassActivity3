def main():
    userInput = input("Enter your word to sentence to see word count: ")
    splitInput = userInput.split()

    print("Your word count is:",len(splitInput))

if __name__ == "__main__":
    main()
