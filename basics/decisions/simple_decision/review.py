# A program to help Beep decide what to watch on television.

# This program will demonstrate the following skills learnt: Decisions with if..elif..else statements,
# Nested decisions and Multiple conditions (AND, OR, NOT) logical operators

# Retrieve from user type of programme to watch.
print("Should I watch a 'film' or start a 'tv series'?")
type = input()

# Determine which type of programme
if type == "film" or type == "tv series":
    # Retrieve genre type from user
    print(f"\nWhat type of {type} should I watch?")
    genre = input()

    # Determine genre type and display question to retrieve a recommendation from user
    if genre == "drama":
        print(f"\nOoh....a drama {type} - I've never watched one of them before, which do you recommend?")
        name = input()
        # Retrieve the length in minutes of recommended programme
        print(f"\nHow long is {name} to watch (minutes)?")
        time = int(input())

        # Determine length of programme and display correct response
        if time < 150 and not time <= 0:
            print(f"\nGreat, I've got enough time to watch the {type} {name} - now how do you turn on the TV?!")
        elif time >=150:
            print(f"\nWoah! I haven't got enough time for that {type}, I'm sleepy now maybe I'll go for a Zzzzz.")
        else:
            print(f"\nSorry I didn't recognise {time} as minutes, oh my brain hurts now and I... Zzzzzz")

    # Determine genre type and display question to retrieve a recommendation from user
    elif genre == "comedy":
        print(f"\nOoh....a comedy {type} - I love a good comedy, which do you recommend?")
        name = input()

        # Retrieve the length in minutes of recommended programme
        print(f"\nHow long is {name} to watch (minutes)?")
        time = int(input())

        # Determine length of programme and display correct response
        if time < 150 and not time <= 0:
            print(f"\nGreat, I've got enough time to watch the {type} {name} - now how do you turn on the TV?!")
        elif time >= 150:
            print(f"\nWoah! I haven't got enough time for that {type}, I'm sleepy now maybe I'll go for a Zzzzz.")
        else:
            print(f"\nSorry I didn't recognise {time} as minutes, oh my brain hurts now and I... Zzzzzz")

    # Determine genre type and display question to retrieve a recommendation from user
    elif genre == "action":
        print(f"\nWow...an action got to love a good action {type}, which do you recommend?")
        name = input()

        # Retrieve the length in minutes of recommended programme
        print(f"\nHow long is {name} to watch (minutes)?")
        time = int(input())

        # Determine length of programme and display correct response
        if time < 150 and not time <= 0:
            print(f"\nGreat, I've got enough time to watch the {type} {name} - now how do you turn on the TV?!")
        elif time >= 150:
            print(f"\nWoah! I haven't got enough time for that {type}, I'm sleepy now maybe I'll go for a Zzzzz.")
        else:
            print(f"\nSorry I didn't recognise {time} as minutes, oh my brain hurts now and I... Zzzzzz")

    # Determine genre type and display question to retrieve a recommendation from user
    elif genre == "romcom":
        print(f"\nOh ok a romantic comedy {type} , which do you recommend?")
        name = input()

        # Retrieve the length in minutes of recommended programme
        print(f"\nHow long is {name} to watch (minutes)?")
        time = int(input())

        # Determine length of programme and display correct response
        if time < 150 and not time <= 0:
            print(f"\nGreat, I've got enough time to watch the {type} {name} - now how do you turn on the TV?!")
        elif time >= 150:
            print(f"\nWoah! I haven't got enough time for that {type}, I'm sleepy now maybe I'll go for a Zzzzz.")
        else:
            print(f"\nSorry I didn't recognise {time} as minutes, oh my brain hurts now and I... Zzzzzz")

    # Determine genre type and display question to retrieve a recommendation from user
    elif genre == "thriller":
        print("\nOh dear - I'm scared of thrillers, maybe I'll read a book. Can you recommend a good book to read?")
        name = input()
        print(f"\n{name} sounds a great book to read, thank you")

     # Determine genre type and display question to retrieve a recommendation from user
    elif genre == "sci-fi":
      print(f"\nNow you're talking, sci-fi is my kind of {type} , which do you recommend?")
      name = input()

        # Retrieve the length in minutes of recommended programme
      print(f"\nHow long is {name} to watch (minutes)?")
      time = int(input())

        # Determine length of programme and display correct response
      if time < 150 and not time <= 0:
            print(f"\nGreat, I've got enough time to watch the {type} {name} - now how do you turn on the TV?!")
      elif time >= 150:
            print(f"\nWoah! I haven't got enough time for that {type}, I'm sleepy now maybe I'll go for a Zzzzz.")
      else:
            print(f"\nSorry I didn't recognise {time} as minutes, oh my brain hurts now and I... Zzzzzz")
    else:
        print("\nOh dear I don't recognise that genre, maybe I'll read a book. Can you recommend a good book to read?")
        name = input()
        print(f"\n{name} sounds a great book to read, thank you")
elif type == "both":
    print("\nSorry I only have time to watch one of them")

else:
    print("\nSorry I didn't recognise that answer, never mind I think I'll read a book instead.")
