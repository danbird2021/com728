# A program to build an ASCII art ladder to desired size of user, using multiple user defined functions.

def display_ladder(steps):

    """Displays top step and then builds ladder to the amount of steps passed from create_ladder function"""

    print("| |")
    for s in range(steps):
        print("***")
        print("| |")

def create_ladder():

    """Retrieves amount of steps from user and then passes this value via calling display_ladder function"""

    print("How many steps remain?")
    steps = int(input())

    display_ladder(steps)
def run():
    create_ladder()