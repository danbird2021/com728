# Hangman Game



def lives_left(guesses_left,display_word, word, guessed_letters):


    if guesses_left <= 10:
        base = "__________"
    else:
        base = ""
    if guesses_left <= 9:
        p = "|"
    else:
        p = ""
    if guesses_left <= 8:
        beam = " __________"
    else:
        beam = ""
    if guesses_left <= 7:
        s = "/"
    else:
        s = ""
    if guesses_left <= 6:
        noose = "|"
    else:
        noose = ""
    if guesses_left <= 5:
        head = "0"
    else:
        head = ""
    if guesses_left <= 4:
        body = "|"
    else:
        body = ""
    if guesses_left <= 3:
        l_arm = "_"
    else:
        l_arm = ""
    if guesses_left <= 2:
        r_arm = "_"
    else:
        r_arm = ""
    if guesses_left <= 1:
        l_leg = "/"
    else:
        l_leg = ""
    if guesses_left == 0:
        r_leg = "\\"
    else:
        r_leg = ""
    print(f"""
        {beam}                      Letters already guessed: {guessed_letters}
        {p} {s}        {noose}
        {p}{s}         {head}
        {p}         {l_arm}{body}{r_arm}
        {p}         {l_leg} {r_leg}
        {p}{base}
       \nWord: {display_word}
       \n{guesses_left} lives left remaining.
        """)
    if guesses_left <= 0:
        exit()
    elif guesses_left > 0:
        get_guess(guesses_left, display_word, word, guessed_letters)


def get_guess(guesses_left,display_word,word, guessed_letters):
    print("Please enter a single letter to guess:")
    guess = input().strip().lower()
    check_guess(guess,word,guesses_left,display_word, guessed_letters)


def check_guess(guess,word,guesses_left,display_word,guessed_letters):
    correct = False
    old_display_word = display_word
    display_word  = ""
    guessed_letters += (f" {guess[0]}")

    for position in range(0, len(word), 1):
        if word[position] == guess[0]:
            display_word += guess[0]
            correct = True
        else:
            display_word += old_display_word[position]

    if  correct == False and guesses_left == 1:
        print("You didn't guess correctly and you lose!")
        print("GAME OVER!")
        print(f"The correct word was: {word}")
        lives_left(0, display_word, word, guessed_letters)
    elif correct == False and guesses_left > 1:
        guesses_left -= 1
        print("You didn't guess correctly!")

        lives_left(guesses_left, display_word, word, guessed_letters)

    elif correct == True:
        print("You guessed correctly!")
        if display_word == word:
            print("Congratulations - You've won!!")
            print(f"The Correct word was: {word}.")
            exit()
        elif guesses_left == 11:
            print(display_word)
            get_guess(guesses_left, display_word, word, guessed_letters)
        else:
            lives_left(guesses_left, display_word, word, guessed_letters)


def get_word():
    print("Welcome to the Hangman Game!")
    print("\nPlease enter word to be used:")
    word = input().strip().lower()
    guessed_letters = ""
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(f"The word has {len(word)} letters.")
    get_guess(11, '_' * len(word) , word, guessed_letters)


get_word()









