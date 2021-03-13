# A program to create a simple set and display it to the user.

def observed():
    """
    Create set 'observations' with the following values:
    "Flying Car", "Sky Scraper", "Sky Scraper", "Laser", "Dome", "Dome"
    and return the set back to the user.
    :return: observations set and it's contents
    """
    observations = {"Flying Car", "Sky Scraper", "Sky Scraper", "Laser", "Dome", "Dome"}

    return observations

def run():
    """
    Call observed function and display results to user.
    :return:
    """
    print(observed())


# Determine if main file is being executed.
if __name__ == "__main__":
    run()
