def run():
    # Program to retrieve a phrase and reverse this using a for loop and the 'in' membership operator,
    # and then display reversed phrased back to the user.

    # Retrieve phrase to be reversed.
    print("What phrase do you see?")
    phrase = input()

    # Declare variable reversed_phrase as a string.
    reversed_phrase = str()

    # Display start message.
    print("\nReversing...")

    # Determine each character in phrase
    for character in phrase:
        # Add reversed_phrase to current chracter in phrase for this iteration
        reversed_phrase = character + reversed_phrase

    # Display complete message with reversed phrase.
    print(f"\nThe phrase is: {reversed_phrase}")
