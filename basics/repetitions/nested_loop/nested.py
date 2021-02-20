def run():
    # A program that allows the user to enter grid dimensions for it to be filled
    # with an ASCII emoji using nested for loops.

    # Retrieve number of rows and columns from user
    print("How many rows should I have?")

    rows = int(input())

    print("How many columns should I have?")

    columns = int(input())

    # Display start message.
    print("Here I go:\n")

    # Display grid using dimensions set out by user input and fill with ASCII emoji.

    # For every row in rows perform inner for loop. Start at 0, stop at rows, increment each interation by 1.
    for row in range(0, rows, 1):

        # For every col in columns display ASII emoji, stay on the same line. Start at 0, stop at cols, increment each interation by 1.
        for col in range(0, columns, 1):
            print(f":-)", end="")
        print()

    # Display complete message.
    print("\nDone!")