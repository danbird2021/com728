# A program using a while loop to help Beep remove cables holding a robot.

# Retrieve amount of cables to be removed.
print("How many cables should I remove?")
cables = int(input())

# Declare variable to count cables removed.
cables_removed = 0

# Blank line
print("")

# While cables_removed is less than cables
while cables_removed < cables:

    # Update cables_removed count.
    cables_removed += 1

    # Display finished message.
    print("Removed cable.")