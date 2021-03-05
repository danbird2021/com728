def directions():
    """
    Create a list called directions with a number of strings.
    Return list directions to user.
    :return: Directions list
    """
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def run():
    """
    Call Directions function and display to user the results.
    :return: none.
    """
    print (directions())

run()