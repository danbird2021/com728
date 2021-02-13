# A program to retrieve markings seen by Beep and Bop in the Cave via user input.
# Using a for loop and the range function to display each character and it's relevant index position.


# Retrieve markings seen.
print("What strange markings do you see?")
markings = input()

# Display start message.
print("\nIdentifying...\n")

# Determine character length of markings seen and create a range to that length,
# starting at index position 0 and step through each iteration by 1.
for position in range(0, len(markings), 1):

    # Display index position of current character with relevant character within markings string of this iteration.
    print(f"index {position}: {markings[position]}")

# Display complete message.
print("\nDone!")