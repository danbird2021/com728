import os

def display_chars(file_path, num_chars):
    with open(file_path) as file:
        partial_data = file.read(num_chars)
    print("The first 5 characters are:")
    print(f"{partial_data}\n")

def display_line(file_path):
    with open(file_path) as file:
        line = file.readline().strip()
    print("The first line is:")
    print(f"{line}\n")

def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
    print("The full text is:")
    print(f"{data}\n")




def run():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")

if __name__ == "__main__":
    run()