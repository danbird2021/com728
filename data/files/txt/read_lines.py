# A program to read a text file line by line using the open method and a for loop.
# Each line can be displayed back to the user individually with necessary print statements at each stage.


def search(file_path):
    """
    Display to user searching message. Using the open method and file_path parameter passed to function,
    open as file.
    Using a for loop, loop through each line of file and display back to user each lines' content with the
    message 'Looked in' proceeding. Once all lines in the file have been read and displayed back to user,
    display done message to user.

    :param file_path: file_path of file to be read line by line.
    :return: none.
    """
    print("Searching...")
    # Do everything with file here:
    with open(file_path) as file:
        for location in file:
            print(f"Looked in {location.strip()}")
    print("...Done!")


def run():
    """
    Call search function and pass file_path parameter "library.txt"
    in order for the search function to display each line of the text file individually.
    :return: none.
    """
    search("library.txt")


# Call run function.
run()