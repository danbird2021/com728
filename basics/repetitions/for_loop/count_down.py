def run():
    # A program that uses the for loop to count down the number of steps away,
    # that Beep and Bop are from the cave.

    # Retrieve number of steps to be displayed.
    print("How far are we from the cave?")
    num_of_steps = int(input())

    # Blank line
    print("")

    # Display each step remaining - count in range (start with num_of_steps, stop with 0, step -1 for each iteration of loop
    for count in range(num_of_steps, 0, -1):
        # Determine count number and display 'step' when count equals 1 everything else equals 'steps'
        if count == 1:
            print(f"{count} step remaining")
        else:
            print(f"{count} steps remaining")

    # Display completed message
    print("\nWe have reached the cave!")