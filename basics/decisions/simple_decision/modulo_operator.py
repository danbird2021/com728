#a program to determine if user enters an odd or even number

print("Please enter a whole number:")
number = int(input())


# if statement using modulo operator to determine odd or even number
if number % 2 != 0:
    print(f"The number {number} is odd.")
else:
    print(f"The number {number} is even.")
