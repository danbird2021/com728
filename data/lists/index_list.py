def movements():
    """
    Create a list called path with the following elements :"Move Forward", 10, "Move Backward", 5,
    "Move Left", 3, "Move Right", 1.
    Return list path to user.

    :return: List path with it's entire contents
    """
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]

    return path

def run():
    """
    Call movements function, then Display to the user Moving message.
    Retrieve path list from movements function and place in variable path_list.
    Using a for loop, display back to the user the movement and number of steps and iterate through in steps of 2.
    Starting at index value 0 and finish at length of path_list.
    :return: none.
    """
    print("Moving...")
    path_list = movements()

    for m in range (0, len(path_list), 2):
        print(f"{path_list[m]} for {path_list[m+1]} steps")


run()
