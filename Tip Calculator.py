# Prompt the user to enter the bill amount
print("Please enter the bill amount: ")
bill_amount = float(input())

# Prompt the user to enter a tip percentage
print("Please enter the tip percentage (e.g. 15 for 15%): ")
tip_percentage = float(input())

# Calculating Tip Amount
tip_amount = bill_amount * (tip_percentage / 100)

# Calculate the total amount
total_amount = bill_amount + tip_amount

# Output
print(f"Bill amount: ${bill_amount:.2f}")
print(f"Tip amount: ${tip_amount:.2f}")
print(f"lump sum: ${total_amount:.2f}")
