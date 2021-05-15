def main():
    userInput = input("Enter your word to sentence to see word count: ")
    splitInput = userInput.split()

    print(len(splitInput))

if __name__ == "__main__":
    main()
