# A program to demonstrate the use of user-defined functions with multiple parameters

def climb_ladder(steps_remaining, steps_crossed):
    """
    Retrieve amount of steps remaining and amount of steps crossed,
    and determine if amount of steps remaining is greater than steps crossed.
    Finally display a correct response.
    """
    if steps_remaining > steps_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")

def run():
    climb_ladder(5, 2)
    climb_ladder(2, 5)
