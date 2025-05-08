# Function to calculate the salary for each day and total pay
def calculateSalary(days):
    totalPay = 0 # initialize total pay in pennies
    salary = 0.01 # Starting salary (1 penny)

    # Display the header for the table
    print("Day\tSalary (in dollars)")
    print("-----------------------------")

    # Calculate and display the salary for each day
    for day in range(1, days + 1):
        print(f"{day}\t${salary:.2f}") # Display salary for the day in dollars
        totalPay += salary # Add the salary to the total pay
        salary *= 2 # Double the salary for the next day

    # Display the total pay after all the days
    print("-----------------------------")
    print(f"Total pay after {days} days: ${totalPay:.2f}")

# Main Program
if __name__ == "__main__":
    # Ask the user for the number of days
    daysInput = input("Enter the number of days: ")

    # Check if input is valid and convert to integer
    if daysInput.isdigit():
        numDays = int(daysInput)
        calculateSalary(numDays)
    else:
        print("Please enter a valid number of days.")
