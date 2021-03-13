# A program to create a simple dictionary and iterate through the dictionary.

def pattern():
    """
    Create a dictionary called sequences and populate with the following items:
    " "Short Sequence":3, "Medium Sequence":2, "Long Sequence":1 ".
    return sequences dictionary and it's contents.

    :return: sequences dictionary
    """
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences


def display_keys(data):
    """
    Display to user 'Keys:' heading. Using a for loop and the method 'keys',
    for each iteration display the current key of the sequences dictionary
    passed via the data parameter.

    :param data: sequences dictionary
    """
    print("\nKeys:")
    for key in data.keys():
        print(key)

def display_values(data):
    """
    Display to user 'Values:' heading. Using a for loop and the method 'values',
    for each iteration display the current value of the sequences dictionary
    passed via the data parameter.

    :param data: sequences dictionary
    """
    print("\nValues:")
    for value in data.values():
        print(value)

def display_items(data):
    """
    Display to user 'Pairs:' heading. Using a for loop and the method 'items',
    for each iteration display the current key value pair of the sequences dictionary
    passed via the data parameter.

    :param data: sequences dictionary
    """
    print("\nPairs:")
    for key, value in data.items():
        print(f"{key}: {value}")

def run():
    """
    Call display_keys() function and pass the returned value from the pattern() function.
    Next call display_values() function and pass the returned value from the pattern() function.
    Finally call display_items() function and pass the returned value from the pattern() function.
    """
    display_keys(pattern())
    display_values(pattern())
    display_items(pattern())


# Determine if main file is being executed.
if __name__ == "__main__":
    run()
