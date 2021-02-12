# A program to allow Beep to pick an adventure using the logical OR operator within an If statement.

# Retrieve from user adventure type.
print("What type of adventure should I have?")
adventure = input()

# Determine which adventure using the OR operator and display an appropriate response to user.
if adventure == "scary" or adventure == "short":
    print("\nEntering the dark forest!")
elif adventure == "safe" or adventure == "long":
    print("\nTaking the safe route!")
else:
    print("\nNot sure which route to take.")
