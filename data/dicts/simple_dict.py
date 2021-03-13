# A program to create a simple dictionary

def pattern():
    """
    Create a dictionary called sequences and populate with the following items:
    " "Short Sequence":3, "Medium Sequence":2, "Long Sequence":1 ".
    return sequences dictionary and it's contents.

    :return: sequences dictionary
    """
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences

def run():
    """
    Call pattern function and display to the user returned results.
    """
    print(pattern())


# Determine if main file is being executed.
if __name__ == "__main__":
    run()
