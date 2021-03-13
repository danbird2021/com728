# A program to allow the user to sort and manipulate a set.

def observed():
    """
    Create a list called observations. Retrieve from user 7 observations in string form
    using a for loop. Each iteration display to user "Please enter an observation:' retrieve the
    response and append to the end of the list observations.
    Finally return observations list.

    :return: observations list
    """
    observations = []
    for o in range(5):
        print("Please enter an observation:")
        response = input()
        observations.append(response)

    return observations

def remove_observations(list_of_obs):
    """
    Display to user question to see if they wish to remove an observation, the response from user in the form of yes or no
    to be placed in the variable response. If the user says yes then display to user question to ask which observation in
    string form they wish to be removed from list_of_obs list. Remove the first instance of this string in the list.
    Once the user wishes to no longer remove observations, return amended list of observations.
    :param list_of_obs: list of observations
    :return: amended list of observations
    """
    removing = True
    while removing == True:
        print("Do you wish to remove an observation (yes/no)?")
        response = input()
        if response == "yes":
            print("What observation do you wish to remove?")
            remove = input()
            list_of_obs.remove(remove)
        else:
            removing = False

    return list_of_obs


def run():
    """
    Display to the user counting message. Call observed_list() function and place return results in
    the variable observed_list. next Call removed_observations() function and pass parameter observed_list.
    Place new amended list in returned_list variable. Create observations_set set.

    For each iteration of the length of returned_list, place the value in a variable called obs_value,
    next count the amount of times the value appears in the obs_list and place the count in the variable
    obs_count. Place these two variables in a tuple and add it to the set observations_set.

    For each tuple in the sorted version of the set observations_set display to the user the first element and the second element in a print statement,
    to display the string value from the user and how many times it was entered.
    """
    print("Counting observations...")
    observed_list = observed()
    returned_list = remove_observations(observed_list)

    observations_set = set()

    for value in range(len(returned_list)):
        obs_value = returned_list[value]
        obs_count = returned_list.count(obs_value)
        observations_set.add((obs_value, obs_count))



    for item in sorted(observations_set):
        print(f"{item[0]} observed {item[1]} times.")


# Determine if main file is being executed.
if __name__ == "__main__":
    run()
