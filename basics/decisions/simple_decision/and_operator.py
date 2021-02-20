def run():
    # A program to help Beep decide to go deeper into the forest or find a way out,
    # using the logical AND operator within an IF statement.

    # Retrieve from user what Beep heard and saw
    print("What did I hear?")
    heard = input()

    print("\nWhat did I see?")
    saw = input()

    # Identify what was seen and heard and display appropriate response.

    if heard == "grrr" and saw == "two red eyes":
        print("\nThere is a scary creature. I should get out of here!")
    else:
        print("\nI am a little scared but I will continue.")