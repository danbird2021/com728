def likelihood():
    likelihoods = ()
    likelihoods = (50, 38, 27, 99, 4)

    return (min(likelihoods), max(likelihoods))


def run():
    likelihood_tuple = likelihood()
    min_likelihood = likelihood_tuple[0]
    max_likelihood = likelihood_tuple[1]
    print(f"Minimum likelihood of falling: {min_likelihood}%")
    print(f"Maximum likelihood of falling: {max_likelihood}%")



# Determine if main file is being executed.
if __name__ == "__main__":
    run()