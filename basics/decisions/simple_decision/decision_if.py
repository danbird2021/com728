def run():
    # Program to ask user what book Beep should read.

    # ask user for book type
    print(f"What type of book is this?")
    book_type = input()

    # if user enters 'adventure' as book type then display 'I like adventure books!' message
    if book_type == 'adventure':
        print("I like adventure books!")

    print("Finished reading book!")
