# A program using a while loop and len() function to allow the robot to communicate with Beep

# Retrieve phrase from user.
print("Please enter a phrase:")
phrase = input()

# Character length of phrase.
phrase_length = int(len(phrase))

# Variable to count number of times Bop is printed.
count = 0

# While count is less than phrase length.
while count < phrase_length :

# Update count by 1
    count += 1

# Display 'Bop ' and keep on same line.
    print(f"Bop ",end ='')
