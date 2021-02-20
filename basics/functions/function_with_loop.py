# A program to demonstrate the use of a user-defined function with a loop.

def cross_bridge(distance):
    """
    Retrieves amount of steps from user, using a for loop to display 'Crossed step.' for each iteration.
    Finally an if statement to display certain responses depending on amount of steps received.
    """
    for s in range(distance):
        print("Crossed step.")

    if distance >=5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")

def run():
    cross_bridge(3)
    cross_bridge(6)