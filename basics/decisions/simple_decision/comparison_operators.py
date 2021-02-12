# a program to determine which number given by the user from two numbers is the smallest
print("Please enter the first number:")
first_number = int(input())

print("Please enter the second number:")
second_number = int(input())

#if/elif/else statement to determine which number is the smallest or if they are equal
if first_number < second_number:
    print("The first number is the smallest.")
elif first_number > second_number:
    print("The second number is the smallest.")
else:
    print("Both are equal!")