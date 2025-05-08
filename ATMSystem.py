# Created a class named "BankAccount" that declares account number, balance, and pin
class Account:
    def __init__(self, accountNumber, balance, pin):
        self.accountNumber = accountNumber
        self.balance = balance
        self.pin = pin

    def getBalance(self):
        return self.balance

    def setBalance(self, amount):
        self.balance = amount

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insfficient funds or invalid amount.")
class CashDispenser:
    def activateCashDispenser(self, amount):
        print(f"Dispensing ${amount:.2f} in cash. Please Wait.")

class ReceiptPrinter:
    def printReceipt(self, transactionType, amount, balance,accountNumber):
        print(f"\n------------------------------\n")
        print(f"Reciept: {transactionType}")
        print(f"Account Number: {accountNumber}")
        print(f"Amount: ${amount:.2f}")
        print(f"New Balance: ${balance:.2f}")
        print(f"\n-------------------------------\n")

class Customer:
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def deposit(self, amount):
        self.account.deposit(amount)

    def withdraw(self, amount, cashDispenser, receiptPrinter):
        if amount > 0 and self.account.getBalance() >= amount:
            self.account.withdraw(amount)
            cashDispenser.activateCashDispenser(amount)
            receiptPrinter.printReceipt("Withdrawal", amount, self.account.getBalance(),
                                        self.account.accountNumber)

        else:
            print("Transaction failed: Insufficient funds.")

    def checkBalance(self):
        print(f"Current balance: ${self.account.getBalance():.2f}")

# Main Function
def main():
    account = Account("1466066", 1500.00, "1234")
    customer = Customer("Silver Carbajal", account)
    cashDispenser = CashDispenser()
    receiptPrinter = ReceiptPrinter()

    customer.deposit(350)
    print()
    customer.withdraw(200, cashDispenser, receiptPrinter)
    print()
    customer.checkBalance()

if __name__ == "__main__":
    main()
