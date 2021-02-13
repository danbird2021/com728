# A program to use look at a given sequence and find the number of characters between two
# identified markers within the sequence using a for loop.

# Retrieve sequence and specified character from user.
print("Please enter a sequence:")
sequence = input()

print("Please enter a character:")
character = input()

# Declare variable distance and set to 0 - to keep a count of number of characters between two markers.
distance = 0

# Declare variable counting and set to false to keep track of when counting amount of characters or not.
counting = False

# Determine characters within sequence and for each iteration perform if statement.
for char in sequence:
        # Determine if the first marker has been found if so then start counting.
         if char == character and counting == False:
                counting = True
          # Determine if character is not a marker if so then add 1 to the distance variable.
         elif char != character and counting == True:
             distance += 1
         # Determine if final marker has been reached, if so stop counting.
         elif char == character and counting == True:
             counting = False

# Display completed message with distance between markers.
print(f"The distance between the markers is {distance}.")