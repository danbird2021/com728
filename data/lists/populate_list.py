def directions():

    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]

    return directions

def menu():
    print("Please select a direction:")
    directions_list = directions()

    for m in range(len(directions_list)):
        print(f"{m}: {directions_list[m]}")

    response = int(input())
    return directions_list[response]

def run():
    route = []
    print("Working out escape route...\n")

    for escape in range(0, 5, 1):
        route.append(menu())

    print(f"Escape route: {route}")

# Determine if main file is being executed.
if __name__ == "__main__":
    run()
