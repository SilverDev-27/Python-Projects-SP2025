# Get the number of males and females
males = int(input("Enter the number of males in the class: "))
females = int(input("Enter the number of females in the class: "))

# Calculate the total number of students
totalStudents = males+females

# Calculate the percentage of males and females
malePercentage = (males / totalStudents) * 100
femalePercentage = (females / totalStudents) * 100

# Display the results with formatted output
print(f"\nTotal Students: {totalStudents}")
print(f"Percentage of Males: {malePercentage:.2f}%")
print(f"Percentage of Females: {femalePercentage:.2f}%")
