# A program to help Bop calculate the sum of the first 100 numbers using a while loop.

# Display initial message to user.
print("Calculating the sum of the first 100 numbers...")

# Declare sum variable to equal total number to count to.
sum = 100

# Declare count variable to keep a count of numbers that have been added to answer.
count = 0

# Declare answer variable to hold the final result of calculation.
answer = 0

#While count is less than or equal to sum.
while count <= sum:

# Add current count value to answer.
    answer += count

# Update count variable by 1.
    count += 1

# Display final message with final calculation to answer.
print(f"...Done! The answer is {answer}.")