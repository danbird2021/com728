def run():
    # Helping Beep find its spare battery using multiple nested decisions

    # Retrieve which room user wants to look in
    print("Where should I look?")
    response = input()

    # A multiple nested if statement to determine which room the user has suggested to look in.
    # Once a room has been identified another question is asked to determine an area to look within the room,
    # appropriate responses will be given depending on users input at each statement.

    # Identify room
    if response == "in the bedroom":
        print("Where in the bedroom should I look?")
        bedroom_area = input()

        # Identify area to look in

        if bedroom_area == "under the bed":
            print("Found some shoes but no battery")
        else:
            print("Found some mess but no battery.")

    elif response == "in the bathroom":
        print("Where in the bathroom should I look?.")
        bathroom_area = input()

        # Identify area to look in

        if bathroom_area == "in the bathtub":
            print("Found a rubber duck but no battery.")
        else:
            print("Found a wet surface but no battery.")

    elif response == "in the lab":
        print("Where in the lab should I look?")
        lab_area = input()

        # Identify area to look in

        if lab_area == "on the table":
            print("Yes! I found my battery!")
        else:
            print("Found some tools but no battery.")

    else:
        print("I do not know where that is but I will keep looking.")


