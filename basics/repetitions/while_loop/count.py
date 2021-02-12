# A program using a while loop to help Beep avoid live cables holding a robot.

# Retrieve amount of live cables to avoid.
print("How many live cables must I avoid?")
live_cables = int(input())

# Declare variable to count cables removed.
cables_avoided = 0

# Blank line
print("")

# While cables_avoided is less than live_cables
while cables_avoided < live_cables:
    # Update cables_avoided count.
    cables_avoided += 1
    # Display number of cables avoided message.
    print(f"Avoiding...Done! {cables_avoided} live cables avoided.")

    # Display finished message.
print("\nAll live cables have been avoided.")