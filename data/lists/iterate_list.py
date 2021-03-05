def directions():

    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]

    return directions

def menu():
    print("Please select a direction:")
    directions_list = directions()

    for m in range(len(directions_list)):
        print(f"{m}: {directions_list[m]}")

def run():
    menu()


# Determine if main file is being executed.
if __name__ == "__main__":
    run()
