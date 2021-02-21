# Hangman Game




def lives_0(guesses_left,display_word, word, guessed_letters):
    print(f"""
     __________     Letters already guessed: {guessed_letters}
    | /        |
    |/         0
    |         _|_
    |         / \\
    |___________

    \n{display_word}
    \n{guesses_left} lives left remaining.
    """)

    exit()

def lives_1(guesses_left,display_word, word, guessed_letters):
    print(f"""
     __________     Letters already guessed: {guessed_letters}
    | /        |
    |/         0
    |         _|_
    |         /
    |___________
    \n{display_word}
    \n{guesses_left} lives left remaining.
    """)
    get_guess(guesses_left, display_word, word, guessed_letters)

def lives_2(guesses_left, display_word, word, guessed_letters):
    print(f"""
     __________     Letters already guessed: {guessed_letters}
    | /        |
    |/         0
    |         _|_
    |         
    |___________
    \n{display_word}
    \n{guesses_left} lives left remaining.
    """)
    get_guess(guesses_left,display_word, word, guessed_letters)

def lives_3(guesses_left,display_word, word, guessed_letters):
    print(f"""
     __________     Letters already guessed: {guessed_letters}
    | /        |
    |/         0
    |         _|
    |         
    |___________
    \n{display_word}
    \n{guesses_left} lives left remaining.
    """)
    get_guess(guesses_left,display_word, word, guessed_letters)

def lives_4(guesses_left,display_word, word, guessed_letters):
    print(f"""      Letters already guessed: {guessed_letters}
     __________
    | /        |
    |/         0
    |          |
    |         
    |___________
    \n{display_word}
    \n{guesses_left} lives left remaining.
    """)
    get_guess(guesses_left,display_word, word, guessed_letters)

def lives_5(guesses_left,display_word, word, guessed_letters):
    print(f"""
     __________     Letters already guessed: {guessed_letters}
    | /        |
    |/         0
    |          
    |         
    |___________
    \n{display_word}
    \n{guesses_left} lives left remaining.
    """)

    get_guess(guesses_left,display_word, word, guessed_letters)


def lives_6(guesses_left,display_word, word, guessed_letters):
    print(f"""
     __________     Letters already guessed: {guessed_letters}
    | /        |
    |/         
    |          
    |         
    |___________
    \n{display_word}
    \n{guesses_left} lives left remaining.
    """)
    get_guess(guesses_left,display_word, word, guessed_letters)

def lives_7(guesses_left,display_word, word, guessed_letters):
    print(f"""
     __________     Letters already guessed: {guessed_letters}
    | /        
    |/         
    |          
    |         
    |___________
    \n{display_word}
    \n{guesses_left} lives left remaining.
    """)
    get_guess(guesses_left,display_word, word, guessed_letters)

def lives_8(guesses_left,display_word, word ,guessed_letters):
    print(f"""
     __________     Letters already guessed: {guessed_letters}
    |         
    |         
    |          
    |         
    |___________
    \n{display_word}
    \n{guesses_left} lives left remaining.
    """)
    get_guess(guesses_left,display_word, word,guessed_letters)

def lives_9(guesses_left,display_word, word, guessed_letters):
    print(f"""
                    Letters already guessed: {guessed_letters}
    |         
    |         
    |          
    |         
    |___________
   \n{display_word}
   \n{guesses_left} lives left remaining.
    """)
    get_guess(guesses_left,display_word, word,guessed_letters)

def lives_10(guesses_left,display_word, word, guessed_letters):
    print(f"""
                    Letters already guessed: {guessed_letters}
         
         
          
         
    ___________
   \n{display_word}
   \n{guesses_left} lives left remaining.
    """)
    get_guess(guesses_left,display_word, word, guessed_letters)

print("Welcome to the Hangman Game!")


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
        lives_0(0, display_word, word, guessed_letters)
        exit()
    elif correct == False and guesses_left > 1:
        guesses_left -= 1
        print("You didn't guess correctly!")

        if guesses_left == 10:
            lives_10(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 9:
            lives_9(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 8:
            lives_8(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 7:
            lives_7(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 6:
            lives_6(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 5:
            lives_5(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 4:
            lives_4(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 3:
            lives_3(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 2:
            lives_2(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 1:
            lives_1(guesses_left, display_word, word, guessed_letters)

    elif correct == True:
        print("You guessed correctly!")
        if display_word == word:
            print("Congratulations - you've won!!")
            print(f"The correct word was: {word}.")
            exit()
        if  guesses_left == 11:
            print(display_word)
            get_guess(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 10:
            lives_10(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 9:
            lives_9(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 8:
            lives_8(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 7:
            lives_7(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 6:
            lives_6(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 5:
            lives_5(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 4:
            lives_4(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 3:
            lives_3(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 2:
            lives_2(guesses_left, display_word, word, guessed_letters)
        elif guesses_left == 1:
            lives_1(guesses_left, display_word, word, guessed_letters)



def get_word():
    print("\nPlease enter word to be used:")
    word = input().strip().lower()
    guessed_letters = ""
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(f"The word has {len(word)} letters.")
    get_guess(11, '_' * len(word) , word, guessed_letters)

get_word()









