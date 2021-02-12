# A program to help Bop calculate the factorial of a number entered by the user using a while loop.

# Retrieve number to find the factorial of number.
print("Please enter a number:")
number = int(input())

# Blank line.
print("")

# Declare count variable to count each time factorial is times count number.
count = 1

# Declare factorial to hold calculation for factorial of number.
factorial = 1

# While count is less than or equal to number
while count <= number:
    # Factorial equals factorial times count
    factorial = factorial * count
    # Upgrade count by 1
    count += 1

# Display message with final factorial calculation
print(f"The factorial is {factorial}." )