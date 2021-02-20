def run():
    # A program to determine the ASCII character represented by an ASCII code using the built in functions range, abs, int and chr.git add

    # Display start message
    print("Program started!")

    # Retrieve number to determine ASCII character.
    print("Please enter an ASCII code:")
    # Make sure number entered (code) is a positive integar.
    code = abs(int(input()))

    # Determine if number is within range and if it is, retrieve the relevant ASCII character otherwise display error message.
    if code in range(32, 127):
        character = chr(code)
        # Display results message with results.
        print(f"The character represented by the ASCII code {code} is: {character}")
    else:
        # Display error message.
        print("Sorry, the number entered is not a valid ASCII code.")

    # Program finished message.
    print("Program Ended!")

