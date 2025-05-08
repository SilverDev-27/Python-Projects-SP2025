# Function to calculate the sum of positive numbers
def calculateSum():
    totalSum = 0 #Initialize total sum to 0

    while True:
        # Ask the user to input a number
        userInput = input("Enter a positive number (or a negative number to stop): ")

        # Convert the input to a float for flexibility in input
        try:
            number = float(userInput)
            
            # Check if the number is negative, in which case we stop
            if number < 0:
                break
            # Add the number to the total sum
            totalSum += number
        except ValueError:
            print("Please enter a valid number.")

    # Display the total sum after the loop ends
    print(f"The total sum of the positive numbers is: {totalSum}")

# Main program
if __name__ == "__main__":
    calculateSum()
