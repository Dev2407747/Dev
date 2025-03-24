# Get user input for numerator and denominator
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

# Perform the division and handle division by zero
if denominator != 0:
    result = numerator / denominator
    print(f"The result of {numerator} divided by {denominator} is: {result}")
else:
    print("Error! Division by zero.")
