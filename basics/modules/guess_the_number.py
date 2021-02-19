#  A guess the number program which demonstrates the use of import and modules.

def play_guess_the_number():
    """Retrieves a minimum and maximum number, a random number is then generated in that range.
       The user is asked to guess the number, each guess is checked and correct response displayed,
       until number is guessed correctly."""
    import random as rnd
    print("Please enter the minimum value:")
    min_num = int(input())

    print("Please enter a maximum value:")
    max_num = int(input())

    random_num =  rnd.randrange(min_num + 1, max_num)
# Debugging code
#print(random_num)
    print(f"I am thinking of a number between {min_num} and {max_num}. Can you guess what it is?")

    guessing = True

    while guessing == True:
        guess = int(input())
        if guess < random_num:
            print("Your guess is too low.")
            print("Try again:")
        elif guess > random_num:
            print("Your guess is too high.")
            print("Try again:")
        elif guess == random_num:
            print("Congratulations! You guessed my number!")
            guessing == False
        else:
            print("Try again:")


play_guess_the_number()