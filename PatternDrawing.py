# Function to draw the pattern
def drawPattern():
    # Outer Loop for the number of rows
    for i in range(5):
        # Always print the first "#" for each row
        print("#", end="")
        
        # Inner loop to print spaces in between the "#"s
        for j in range(i):
            print(" ", end="")
        
        # Print the last "#" in each row except for the first row
        if i > 0:
            print("#", end="")
        
        # Move to the next line after each row
        print()


        
# Main program
if __name__ == "__main__":
    drawPattern()
