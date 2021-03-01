# A program to read a file using it's relative file_path and display back to user the
# depending on function called a specified amount of characters, a complete line or the complete text.

def display_chars(file_path, num_chars):
    """
    Open file_path from passed file_path parameter as file.
    Using the read method, and passed number of characters parameter,
    retrieve set amount of characters and place in variable partial_data.
    Display partial_data contents back to user.

    :param file_path: file path of file to be read.
    :param num_chars: number of chracters to read from specified file.
    :return: none.
    """
    with open(file_path) as file:
        partial_data = file.read(num_chars)
    print("The first 5 characters are:")
    print(f"{partial_data}\n")


def display_line(file_path):
    """
    Open file_path from passed file_path parameter as file.
    Using the readline method, retrieve first line of file and place in variable line.
    Display line contents back to user.

    :param file_path: file path of file to be read.
    :return: none.
    """
    with open(file_path) as file:
        line = file.readline().strip()
    print("The first line is:")
    print(f"{line}\n")


def display_text(file_path):
    """
    Open file_path from passed file_path parameter as file.
    Using the read method, retrieve complete file contents and place in variable data.
    Display full contents back to user.

    :param file_path: file_path of file to be read.
    :return: none.
    """
    with open(file_path) as file:
        data = file.read()
    print("The full text is:")
    print(f"{data}\n")


def run():
    """
    Call display_chars function and pass the file path parameters "library.txt" to be read and
    number of characters to be displayed from beginning of file via the function.

    Also Call display_line function and pass the file path parameter "library.txt to be read,
    in order for the first line of the file to be displayed to user via the function.

    Finally, call display_text function and pass the file path parameter "library.txt" to be read,
    in order for the function called to display entire contents of the read file.

    :return: none.
    """
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")

# Determine if main file is being executed.
if __name__ == "__main__":
    run()
