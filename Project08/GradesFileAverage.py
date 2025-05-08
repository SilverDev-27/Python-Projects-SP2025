# All new code in already existed functions will have a "New Code" comment beside it
class GradesFile:
    def __init__(self, filename):
        self._fileName = filename
        self._gradesList = self.loadGradesData() # New Code

    # Getter
    def getFileName(self):
        return self._fileName

    # Setter
    def setFileName(self, newFileName):
        self._fileName= newFileName
        
    # New function to load grades from the file
    def loadGradesData(self):
        grades = []
        try:
            with open(self._fileName, 'r') as file:
                for line in file:
                    try:
                        grade = float(line.strip())
                        grades.append(grade)
                    except ValueError:
                        print(f"Skipping invalid grade entry: {line.strip()}")
        except FileNotFoundError:
            print:("Error: File not found.")
        except Exception as e:
            print(f"An unexpected error occurred while loading grades: {e}")
        return grades

    # Revised function to calculate the average using _gradesList
    def calculateAverage(self):
        try:
            grades = self._gradesList
            print("Grades in the file:")
            
            for grade in grades:
                print(grade)
                
            if not grades:
                raise ValueError("No valid grades found in file.")

            return sum(grades) / len(grades)

        except ValueError as ve: # Handles case where no valid grades exist
                print(f"Error: {ve}")
        except Exception as e: # Handles unexpected errors
                print(f"An unexpected error occurred: {e}")
        return None

# Main Function
def main():
    fileName = "Grades.txt" # Name of File to store grades

    try:
        with open(fileName, 'w') as file:
            grades = [85, 93, 88, 79, 83, 95, 97, 100] # Hardcoded grades
            for grade in grades:
                file.write(f"{grade}\n") # This will write each grade on a new line

        gradesFile = GradesFile(fileName) # This created a GradesFile object in main function

        average = gradesFile.calculateAverage() # This calls the calculateAverage method from GradesFile

        if average is not None:
            print(f"The average grade is: {average:.2f}")

    except IOError:
        print("Error: Issue occured while handling the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}") # Handles any other errors

if __name__ == "__main__":
    main()

# Just a quick comment. When I originally ran the code I didn't initialize the _fileName in the GradesFile class (line 3) correctly.
# So my output read "An unexpected error occurred: 'GradesFile' object has no attribute '_fileName'
# Meaning that my Error Methods worked! Code ran fine once I fixed the initialization.
