def run():
    # A program that displays the number of mountains a user enters,
    # using a for loop and ASCII characters.

    # Retrieve number of mountains to be displayed.
    print("How many mountains should I display?")
    num_mountains = int(input())

    # Display starting message.
    print("\nDisplaying...")

    # Display mountains required - count in range (start at 0, end at num_mountains -1, step 1 on each loop).
    for count in range(0, num_mountains, 1):
        print("""
               __
              /  \\_  
             /^    \\
            /  ^    \\_
          _/ ^ ^     ^\\
         /  ^     ^    \\ """)