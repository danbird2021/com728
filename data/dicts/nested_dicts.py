# A program to create a dictionary of dictionaries.

def short_pattern():
    """
    Create pattern dictionary with the following key value pairs: "sequence":"101", "occurrences":5
    Return pattern dictionary and it's contents.

    :return: pattern dictionary
    """
    pattern = {"sequence":"101", "occurrences":5}
    return pattern

def medium_pattern():
    """
    Create pattern dictionary with the following key value pairs: "sequence":"111000", "occurrences": 25
    Return pattern dictionary and it's contents.

    :return: pattern dictionary
    """
    pattern = {"sequence":"111000", "occurrences": 25}
    return pattern

def long_pattern():
    """
    Create pattern dictionary with the following key value pairs: "sequence":"1100110011001100","occurrences":50
    Return pattern dictionary and it's contents.

    :return: pattern dictionary
    """
    pattern = {"sequence":"1100110011001100","occurrences":50}
    return pattern

def run():
    """
    Display Analysing message to user.
    Create a dictionary of dictionaries called sequences. For the first dictionary the key is named "Short Sequence:"
    and the value is the returned value from the short_pattern() function. Next for the second dictionary the key is
    named "Medium Sequence:" and the value is the returned value from the medium_pattern() function. The last
    dictionary the key is named "Long Sequence:" and the value is the returned value from the long_pattern() function.

    Using a for loop and the method 'items' iterate through the sequences dictionary to display each
    key value pair via a print statement.


    """
    print("Analysing patterns...")
    sequences = {"Short Sequence":short_pattern(),"Medium Sequence": medium_pattern(),"Long Sequence": long_pattern()}

    for key, value in sequences.items():
        print(f"{key}: {value}")


# Determine if main file is being executed.
if __name__ == "__main__":
    run()
