# Ask the user to enter a year
year = int(input("Enter a year: "))

# Determine if it is a leap year
if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(f"Februrary in the year {year} has 29 days (Leap Year).")
else:
    print(f"February in the year {year} has 28 days (Not a Leap Year).")

# Program checks if year is divisible by 100: if yes, it must also be divisible by 400 to be a leap year. If no, it must be divisible by 4 fto be a leap year.
