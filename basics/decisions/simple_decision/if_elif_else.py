def run():
    # Program to help Beep learn to paint

    print("Towards which direction should I paint (up, down, left or right)?")
    direction = input()

    # if elif else statement to determine users input and correct response to display to user
    if direction == "up":

        print("I am painting in the upward direction!")

    elif direction == "down":

        print("I am painting in the downward direction!")

    elif direction == "left":

        print("I am painting in the left direction!")

    elif direction == "right":

        print("I am painting in the right direction!")

    else:

        print("I don't know what direction you are painting!")