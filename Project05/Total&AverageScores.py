# The first function I will code is to prompt a valid score between 0 an 100
def getValidScore():
    while True:
        try:
            userInput = float(input("Enter a test score between 0 and 100: "))
            # Then I check if the score is within the valid range
            if 0 <= userInput <=100:
                return userInput
            else:
                print("Whoops! That isn't a valid score. Please enter a score between 0 and 100.")
        # Here I put a ValueError exception just in case the user doesn't enter a number
        except ValueError:
            print("Please enter a number, not text.")

# My next function will be to calculate total and average from the list of scores
def calcTotalAndAverage(testScores):
    total = sum(testScores) # this will add up all the scores
    # If no scores are provided, don't divide by zero
    average = total / len(testScores) if testScores else 0
    return total, average

def main():
    scoresList = [] # I created this array to store valid test scores here
    print("Weelcome to the score tracker!")

    while True:
        score = getValidScore() # This gets a valid score from the user
        scoresList.append(score) # This stores the score in the list
        print(f"Added score: {score}") # This lets the user know that the score was added

        # I will then ask the user if they want to input more scores
        enterMoreScores = input("Do you want to enter another score? (yes/no): ").strip().lower()
        if enterMoreScores != "yes":
            break # If the answer isn't 'yes', stop asking for scores

    # Once the Loop is done, I then calculate the total and average
    totalScore, averageScore = calcTotalAndAverage(scoresList)

    # I then display the results to the user
    print("\nHere's the summary:")
    print(f"Total score of all entries: {totalScore}")
    print(f"Average score: {averageScore}")

# This just calls the main function to start the program
if __name__ == "__main__":
    main()
