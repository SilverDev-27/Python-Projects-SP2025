# I am creating a class called "Person".
# I also added a method so that the user can add their name like we learned last lesson.
class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def whoAmI(self):
        print(f"I am a person. My name is {self.name}.")

    def contactInfo(self):
        print(f"Contact me at {self.phone}.")

# Created a Customer class that inherits Person attributes
# Also added customer number and membership level using last lesson method.
class Customer(Person):
    def __init__(self, name, phone, customerNumber, membershipLevel="Basic"):
        super().__init__(name, phone)
        self.customerNumber = customerNumber
        self.membershipLevel = membershipLevel

    def whoAmI(self):
        print(f"I am a customer. My name is {self.name}, and my customer number is {self.customerNumber}.")

    def membershipDetails(self):
        print(f"Membership Level: {self.membershipLevel}")

# Main Function
def main():
    person = Person("Silver Carbajal", "123-456-7890")
    customer = Customer("Ramon Ayala", "098-765-4321", "CUSTOMER-027")

    # Directly calling methods
    person.whoAmI()
    person.contactInfo()
    print(" ")# Adding space for better formatting

    customer.whoAmI()
    customer.contactInfo()
    customer.membershipDetails()

if __name__ == "__main__":
    main()
