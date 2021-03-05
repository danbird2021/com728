def likelihood():
    likelihoods = ()
    likelihoods = (50, 38, 27, 99, 4)

    return min(likelihoods)

def run():
    min_likelihood = likelihood()
    print(f"Minimum likelihood of falling: {min_likelihood}%")


# Determine if main file is being executed.
if __name__ == "__main__":
    run()