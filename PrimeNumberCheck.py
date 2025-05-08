# I created a function called checkIfPrime to see if a number is prime
def checkIfPrime(numberToCheck):
    # I first check if the number is less than 2, as it's not prime
    if numberToCheck < 2:
        return False

    # I put in a loop to check for divisibility by numbers up to the square root of the number
    for potentialFactor in range(2, numberToCheck):
        # If I find any factor that divides evenly, the number is not prime
        if numberToCheck % potentialFactor == 0:
            return False

    # If no factors are found, the number is prime
    return True

# Now I made the main function to get user input and show results
def main():
    # I ask the user to enter a number to test if it's prime
    userInput = int(input("Please enter a number to test if it's prime: "))

    # I call the checkIfPrime function to determine if the number is prime
    isPrimeNumber = checkIfPrime(userInput)

    # I then give feedback to the user based on whether the number is prime
    if isPrimeNumber:
        print(f"{userInput} is a prime number!")
    else:
        print(f"{userInput} is not a prime number.")

# Now I run the program when this script is executed
if __name__ == "__main__":
    main()

# End of Assignment
