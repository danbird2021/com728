def run():
    # Program to retrieve a phrase and reverse this using a for loop and the range function,
    # and then display reversed phrased back to the user.

    # Retrieve phrase to be reversed.
    print("What phrase do you see?")
    phrase = input()

    # Declare variable reversed_phrase as a string.
    reversed_phrase = str()

    # Display start message.
    print("\nReversing...")

    # Determine the range size by length of phrase and start iterations at the last index position -1 ending at the first index position -1
    # increment each iteration by -1.

    for position in range(len(phrase) - 1, -1, -1):
        # Add current character at current position of the range of phrase to the variable reversed_phrase.
        reversed_phrase += phrase[position]

    # Display complete message with reversed phrase.
    print(f"\nThe phrase is: {reversed_phrase}")