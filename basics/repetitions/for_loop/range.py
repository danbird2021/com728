def run():
    # A program using the range function in a for loop to adjust light levels of Beep and Bop's night vision.

    # Retrieve an even numbered brightness level from user.
    print("What level of brightness is required (even number)?")
    brightness_level = int(input())

    # Determine if brightness level is an even number if not continue asking user for level until it is even
    while brightness_level % 2 != 0:
        # Retrieve an even numbered brightness level from user.
        print("Sorry, please enter an even number:")
        brightness_level = int(input())

    # Display start message.
    print("\nAdjusting brightness...\n")

    # Display Beep and Bop's brightness levels in increments of 2 using
    # for loop - count in range start at 2, then stop at brightness level + 1, step by 2 for each interation of loop
    for count in range(2, brightness_level + 1, 2):
        print(f"Beep's brightness level: {'*' * count}")
        print(f"Bop's brightness level: {'*' * count}\n")

    # Display complete message.
    print("Adjustments complete!")







