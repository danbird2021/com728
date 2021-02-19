# A program that determines the ASCII code for a character using the built in functions ord and len.

# Display start message
print("Program Started!")

# Retrieve character to determine ASCII code.
print("Please enter a standard character:")
character = input()

# Determine ASCII code for character retrieved and display result.

# Character retrieved must be a single character otherwise display error message.
if len(character) == 1:

    value = ord(character)
    print(f"The ASCII code for {character} is: {value}.")

    # Program finished message.
    print("Program Ended!")

# Display error message.
else:
    print("Sorry, you must only enter a single character!")