# A program to create a set using tuples from a list.

def observed():
    """
    Create a list called observations. Retrieve from user 7 observations in string form
    using a for loop. Each iteration display to user "Please enter an observation:' retrieve the
    response and append to the end of the list observations.
    Finally return observations list.

    :return: observations list
    """
    observations = []
    for o in range(7):
        print("Please enter an observation:")
        response = input()
        observations.append(response)

    return observations

def run():
    """
    Display to the user counting message:
    Retrieve observations list from observed() function and place in variable obs_list.
    Create set observations_set.
    For each iteration of the length of obs_list, place the value in a variable called obs_value,
    next count the amount of times the value appears in the obs_list and place the count in the variable
    obs_count. Place these two variables in a tuple and add it to the set observations_set.

    For each tuple in the set observations_set Display to the user the first element and the second element in a print statement,
    to Display the string value from the user and how many times it was entered.

    """
    print("Counting observations...")
    obs_list = observed()
    observations_set = set()

    for value in range(len(obs_list)):
        obs_value = obs_list[value]
        obs_count = obs_list.count(obs_value)
        observations_set.add((obs_value, obs_count))

    for item in observations_set:
        print(f"{item[0]} observed {item[1]} times.")




# Determine if main file is being executed.
if __name__ == "__main__":
    run()
