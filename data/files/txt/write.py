# A program to search through a text file and determine different aspects of file using a for loop and
# if statement to,retrieve and reformat, then write results to a new text file.



def search(file_path):
    """
    Display search message to user and declare sections and books variables.
    Using the open method and file_path passed open as file.
    With a for loop check each line of the file using the startswith method and check if the line
    starts with 'Section', determine this using an if statement and if true place line contents in variable sections.
    If it is determined not to be a section then place content of current line in books variable.
    Display to user done message.
    Return to user the variables sections and books (formatted).

    :param file_path: file_path of text file to be searched.
    :return: contents of variables: sections and books (formatted).
    """
    print("Searching...", end="")
    sections = ""
    books = "Books:\n"
    with open(file_path) as file:
        for line in file:
            if line.startswith("Section"):
                sections += (line)
            else:
                books += (line)
    print("Done!")
    return (f"{sections}\n\n{books}")


def save(file_path, data):
    """
    Display saving  message to user.
    Using open method open file_path retrieved in write mode as file.
    The write method is used next to store content from data parameter sent to function.
    Display done message to user.

    :param file_path: file path of file to be stored to.
    :param data: data to be stored to file specified.
    :return: none.
    """
    print("Saving...", end="")
    with open(file_path, "w") as file:
        file.write(data)
    print("Done!")


def run():
    """
    Call search function and pass file_path parameter "books.txt", place returned data in variable 'data'.
    Next call save function and pass file_path "section-books.txt" of file to be saved to and pass all contents
    of data variable, in order for contents to be stored via function to specified file.
    :return: none.
    """
    data = search("books.txt")
    save("section-books.txt", data)

# Call run function
run()