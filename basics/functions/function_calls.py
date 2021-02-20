# A program to retrieve a word and give user different options
# to manipulate the word using multiple user defined functions and function calls.

def display_box(word):
    """Retrieved word and display an ASCII art box around the word and display to user"""
    content = f"* {word} *"
    print("*" * ( len(content) ))
    print(content)
    print("*" * ( len(content) ))

def display_lowercase(word):
    """Transform word retrieved into all lower-case letters and display result to user."""
    print(str.lower(word))

def display_uppercase(word):
    """Transform word retrieved into all upper-case letters and display result to user."""
    print(str.upper(word))

def display_mirror(word):
    """Retrieve word and display to user original word along side mirrored version of word."""
    reversed_word = str()
    for position in range(len(word) - 1, -1, -1):

        reversed_word += word[position]

    print(f"{word} | {reversed_word}")

def display_repeat(word):
    """Retrieve word and ask user amount of times to repeat word. Display the word back
    to user this many times alternating between lower-case and upper-case letters."""
    print(f"How many times would you like to display the word {word}?")
    repeat = int(input())
    if repeat % 2 == 1:
        display_lowercase(word)
        repeat -= 1

    while repeat > 0:
        display_uppercase(word)
        display_lowercase(word)
        repeat -= 2

def run():
    """Retrieve desired word from user, display manipulation options back to user and retrieve desired option.
     Then call relevant function and pass attribute entered to the function."""
    print("Please enter a word to manipulate:")
    word = input()
    print("""Please choose one of the following options: 
             1) Display in a Box – display the word in an ascii art box
             2) Display Lower-case – display the word in lower-case e.g. hello
             3) Display Upper-case – display the word in upper-case e.g. HELLO 
             4) Display Mirrored - display the word with its mirrored word e.g. Hello | olleH
             5) Display Repeat - display the word as many times desired alternating between upper-case and lower-case""")
    print("Simply enter a number:")
    option = int(input())

    if option == 1:
        display_box(word)
    elif option == 2:
        display_lowercase(word)
    elif option == 3:
        display_uppercase(word)
    elif option == 4:
        display_mirror(word)
    elif option == 5:
        display_repeat(word)
    else:
        print("Sorry, you needed to enter a number between 1 and 5!")
