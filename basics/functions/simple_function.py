# A program to use a simple function which asks the user for a sound and this is displayed back to the user after the function is called.

# Define Listen function
def listen():
    print("What did you hear?")
    sound = input()
    print(f"That was a loud {sound}!")

def run():
    # Call Listen function
    listen()