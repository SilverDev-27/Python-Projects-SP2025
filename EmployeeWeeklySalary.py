# Class for Employee
class Employee:
    def __init__(self, name, position, hoursWorked):
        self.__name = name
        self.__position = position
        self.__hoursWorked = hoursWorked if hoursWorked >= 0 else 0

    # Setters
    def setName(self, name):
        self.__name = name

    def setPosition(self, position):
        self.__position = position

    def setHoursWorked(self, hoursWorked):
        self.__hoursWorked = hoursWorked

    # Getters
    def getName(self):
        return self.__name

    def getPosition(self):
        return self.__position
    
    def getHoursWorked(self):
        return self.__hoursWorked

    # Method to Calculate weekly salary
    def calculateWeeklySalary(self):
        regularRate = 20
        if self.__hoursWorked > 40:
            overtimeHours = self.__hoursWorked - 40
            salary = (40 * regularRate) + (overtimeHours * regularRate * 1.5) # This calculation allows the employee to get payed their regular hours and if they have overtime hours it calculates their hours plus regularRate * 1.5 which would be 20 * 1.5 = $35
        else:
            salary = self.__hoursWorked * regularRate
        return salary

    def __str__(self):
        return f"Employee(name: {self.__name}, position: {self.__position}, hoursWorked: {self.hoursWorked})"

# Main Function
def main():
    # Two employee objects
    emp1 = Employee("Silver Carbajal", "Web Developer", 50)
    emp2 = Employee("Benny Rodriguez", "Data Analyst", 35)

    # Print Employee Info
    print(f"Employee 1: {emp1.getName()}, {emp1.getPosition()}, Hours Worked: {emp1.getHoursWorked()}, Weekly Salary: ${emp1.calculateWeeklySalary()}")
    print(f"Employee 2: {emp2.getName()}, {emp2.getPosition()}, Hours Worked: {emp2.getHoursWorked()}, Weekly Salary: ${emp2.calculateWeeklySalary()}")

if __name__ == "__main__":
    main()
