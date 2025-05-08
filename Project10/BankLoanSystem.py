class Loan:
    def __init__(self, loanNumber, principal, interestRate, startDate, duration):
        self.loanNumber = loanNumber
        self.principal = principal
        self.interestRate = interestRate
        self.startDate = startDate
        self.duration = duration # (in years)

    # Method that takes the formula and calculates monthly payment
    def monthlyPayment(self):
        r = (self.interestRate / 100) / 12 # this changes the annual interest to monthly rate
        n = self.duration * 12
        if r == 0:
            return self.principal / n # Avoids ZeroDivisionError
        else:
            return self.principal * (r * (1+r) ** n) / ((1+r) ** n - 1) # Formula given

# AutoLoan class that will inherit from loan and add VIN
class AutoLoan(Loan):
    def __init__(self, loanNumber, principal, interestRate, startDate, duration, vinNumber):
        super().__init__(loanNumber, principal, interestRate, startDate, duration)
        self.vinNumber = vinNumber

# Mortgage class that will also inherit from loan, but instead will add address and PIN
class Mortgage(Loan):
    def __init__(self, loanNumber, principal, interestRate, startDate, duration, address, pin):
        super().__init__(loanNumber, principal, interestRate, startDate, duration)
        self.address = address
        self.pin = pin

# Customer class to hold their info and their loans
class Customer:
    def __init__(self, name, phone, address, customerNumber):
        self.name = name
        self. phone = phone
        self.address = address
        self.customerNumber = customerNumber
        self.loans = [] # This allows me to store both auto loans and mortgages into an array

    # Method to add a loan to the customer's profile
    def addLoan(self, loan):
        self.loans.append(loan) # I went ahead and used the .append method taught in the previous assignment

    # This method is to show the monthly payment for each of the customer's loans
    def showMonthlyPayments(self):
        print(f"\nCustomer: {self.name} (#{self.customerNumber})")
        for loan in self.loans:
            loanType = "Auto Loan" if isinstance(loan, AutoLoan) else "Mortgage"
            print(f"{loanType} - Loan #{loan.loanNumber} | Monthly Payment is: ${loan.monthlyPayment():.2f}")

# Main Program to test the classes
def main():
    customer = Customer("Silver Carbajal", "123-456-7890", "2187 Rodeo Dr", "CUST027")

    # Auto Loans
    loan1 = AutoLoan("A1001", 27000, 4.6, "2019-14-05", 6, "VIN98765")
    loan2 = AutoLoan("A1002", 54500, 3.5, "2025-27-06", 4, "VIN12458")

    # Mortgage Loans
    mort1 = Mortgage("M2001", 30000, 3.25, "2012-21-03", 30, "367 Cottage Grove", "PIN8954")
    mort2 = Mortgage("M2002", 45250, 2.75, "2014-18-10", 15, "252 LaGrange Rd", "PIN6935")

    # Adding loans to customer's profile
    customer.addLoan(loan1)
    customer.addLoan(loan2)
    customer.addLoan(mort1)
    customer.addLoan(mort2)

    # Display the list of customer's loans
    customer.showMonthlyPayments()

# Run Program
if __name__ == "__main__":
    main()
