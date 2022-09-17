def main():
    #1. Create a greeting for your program.
    print("Welcome to my band name generator.")
    #2. Ask the user for the city that they grew up in.
    userCity = input("What city did you grow up in?\n")
    #3. Ask the user for the name of a pet.
    petName = input("What is your favorite pet's name?\n")
    #4. Combine the name of their city and pet and show them their band name.
    print("Your band name is " + userCity + " " + petName + "!")
    #5. Make sure the input cursor shows on a new line, see the example at:
    #   https://replit.com/@appbrewery/band-name-generator-end

if __name__ == "__main__":
    main()