# Get the Length and Width of the first rectangle
length1 = float(input("Enter the length of the first rectangle: "))
width1 = float(input("Enter the width of the first rectangle: "))

# Get the Length and Width of the second rectangle
length2 = float(input("Enter the length of the second rectangle: "))
width2 =float(input("Enter the width of the second rectangle: "))

# Calculate the area of both rectangles
area1 = length1 * width1
area2 = length2 * width2

# Compare the areas
print("\nResults:")
print(f"Area of the first rectangle: {area1}")
print(f"Area of the second rectangle: {area2}")

if area1 > area2:
    print("The first rectangle has the greater area.")
elif area2 > area1:
    print("The second rectangle has the greater area.")
else:
    print("Both rectangles have the same area.")
