# A program to help Bop get some numbers and add them together using a while loop.

# Retrieve amount of numbers to be summed up.
print("How many numbers should I sum up?")
amount_of_numbers = int(input())


# Declare count variable to keep a count of numbers that have been added to answer.
count = 0

# Declare answer variable to hold the result of calculation.
answer = 0

# Blank line.
print("")

# While count is less than amount_of_numbers.
while count < amount_of_numbers:
    # Retrieve number and display current number to enter of total amount of numbers.
    print(f"Please enter number {count + 1} of {amount_of_numbers}:")
    # Place users' new number in number variable.
    number = int(input())
    # Add current user number to answer total.
    answer += number
    # Upgrade count by 1.
    count += 1

# Display message with final answer calculation.
print(f"\nThe answer is {answer}.")