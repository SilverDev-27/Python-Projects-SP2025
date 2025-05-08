# Ask the user to enter a person's age
age = int(input("Enter a person's age: "))

# Determine the age category
if age <= 1:
    print("The person is an infant.")
elif age < 13:
    print("The person is a child.")
elif age < 20:
    print("The person is a teenager.")
else:
    print("The person is an adult.")
