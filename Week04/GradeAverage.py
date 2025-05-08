# This is a function that calculates the average of the given scores
def findAverage(scoreList):
    totalSum = sum(scoreList)
    average = totalSum / len(scoreList)
    return average

# This is a function that assigns a Letter grade based on the score
def getGradeFromScore(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# In Main process I'm going to collect scores/ calculate average/ display the grade
def collectScoresAndGrade():
    inputScores = []

    print("Please provide the following 5 test scores:")

    # The Loop to input each score that also has error handling for invalid inputs
    for counter in range(1, 6):
        while True:
            try:
                enteredScore = float(input(f"Enter score {counter}: "))
                if 0 <= enteredScore <= 100:
                    inputScores.append(enteredScore)
                    break
                else:
                    print("Scores must be between 0 and 100. Please re-enter the score.")
            except ValueError:
                print("Invalid input! Please enter a valid numerical value.")


    # Now I will calculate and display the overall average score for all inputs
    averageScore = findAverage(inputScores)
    print(f"\nAverage score: {averageScore:.2f}")

    # For each score i'm going to determine and print the corresponding Letter grade
    print("\nHere are the letter grades for each score:")
    for score in inputScores:
        grade = getGradeFromScore(score)
        print(f"Score: {score} -> Grade: {grade}")

# Now I run the program logic when the script is executed
if __name__ == "__main__":
    collectScoresAndGrade()

# End of Assignment
