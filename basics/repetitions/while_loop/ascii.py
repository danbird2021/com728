# A program using a while loop using ASCII art to help Beep avoid live cables holding a robot.

# Retrieve amount of bars to be charged.
print("How many bars should be charged?")
bars_to_charge = int(input())

# Declare variable to count number of bars charged.
bars_charged = 0

# Blank line
print("")

# While bars_charged is less than bars_to_charge
while bars_charged < bars_to_charge:
    # Update bars_charged count.
    bars_charged += 1
    # Display number of bars charged message with ASCII art.
    print(f"Charging: {'█ ' * bars_charged} ")

    # Display finished message.
print("\nThe battery is fully charged.")