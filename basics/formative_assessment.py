def myth():
    print("Who wishes to learn about the demigod Maui?")
    name = input()
    print(f"Well, {name}, he stole the heart of the goddess Te Fiti.")
    print("You must find Maui and lift the curse!")


def explore(site):
    if site == "The Cavern":
        print("You have found a camakau! You can sail the seas with this.")
    else:
        print("This is just another part of the village.")



def voyage(distance):
    for d in range(distance):
        print("...Crossed some ocean!")
    print("You have found Maui on an island!")


myth()
explore("The Cavern")
explore("The Hut")
voyage(3)