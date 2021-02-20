# A program using a simple function and an if statement which is called
# to return a response to the user depending on the input.

# Define Listen function.
def identify():
    # Retrieve what was seen by user.
    print("What do you see?")
    saw = input()
    # Determine if a large boulder was seen and return the appropriate response.
    if saw == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")

def run():
    # Call listen function.
    identify()