# A program to use a simple function with a parameter and call it with different values

# Define escape_by function
def escape_by(plan):
    # Determine value within parameter plan.
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way1 The boulder is moving too fast!")
    elif plan == "going deeper":
        print("That might just work! Let's go deeper!")
    else:
        print("We cannot escape that way! The boulder is in the way!")

# Call escape_by function with different values.
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")