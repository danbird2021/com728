def run():
    # a program to allow Beep to clasify its books.

    print("What is the cover type (hard or soft) of the book?")

    book_cover = input()

    # nested if statements to determine if book user has entered is soft or hard with extra question to user if soft and correct responses given
    if book_cover == "soft":
        print("Is the book perfect bound?")
        perfect_bound = input()
        if perfect_bound == "yes":
            print("Soft cover, perfect bound books are very popular!")
        else:
            print("Soft covers with coils or stitches are great for short books")
    else:
        print("Books with hard covers can be more expensive!")
