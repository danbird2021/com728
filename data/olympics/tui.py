# A TUI Text based interface for the Olympics case study containing functions to
# display messages and read user's response.

def started(msg=""):
    print('-' * 85)
    print(f"Operations started: {msg}...\n")

def completed():
    print("Operation completed.")
    print('-' * 85)

def error(msg):
    print(f"Error! {msg}")

def menu():
    print("Please select one of the following options:")
    print(f"{'[years]    List unique years':<10}")
    print(f"{'[tally]    Tally up medals':<10}")
    print(f"{'[team]   Tally up medals for each team':<10}")
    print(f"{'[exit]     Exit the program':<10}")
    return input("\nYour selection:")

def display_medal_tally(tally):

    print(f"| {'Gold':<10} | {tally['Gold']:<10}|")
    print(f"| {'Silver':<10} | {tally['Silver']:<10}|")
    print(f"| {'Bronze':<10} | {tally['Bronze']:<10}|")

def display_team_medal_tally(team_tally):

    for countries, medals in team_tally.items():
        print(f"{countries}")
        for medal, count in medals.items():
            if medal == "Gold":
                print(f"{medal:>10}:{count}, ", end="")
            elif medal == "Bronze":
                print(f"{medal}:{count}")
            else:
                print(f"{medal}:{count}, ", end="")

def display_years(years):

    for item in sorted(years, reverse = True):
        print(f"{item}")

