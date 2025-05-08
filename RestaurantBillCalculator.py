# Get the charge for the food from the user
foodCharge = float(input("Enter the charge for the food: $"))

# Calculate the tip (18%) and sales tax(7%)
tip = foodCharge * 0.18
salesTax = foodCharge * 0.07

# Calculate the total amount
totalAmount = foodCharge + tip + salesTax

# Display the results with formatted output
print(f"\nFood Charge: ${foodCharge:.2f}")
print(f"Tip (18%0): ${tip:.2f}")
print(f"Sales Tax (7%): %{salesTax:.2f}")
print(f"Total Amount: ${totalAmount:.2f}")
