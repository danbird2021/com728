# A program to calculate either sum or average of Beep and Bop's weight,
# using the return value with multiple user defined functions.

def sum_weights(beep_weight, bop_weight):
    """Retrieve Beep and Bop's weight and return sum of their weight."""
    return beep_weight + bop_weight

def calc_avg_weight(beep_weight, bop_weight):
    """Retrieve Beep and Bop's weight, calculate the average weight and return result."""
    return (beep_weight + bop_weight) / 2

def run():
    """Retrieve Beep and Bop's weight and choice of sum or average calculation, call relevant function
    and display result back to user."""
    print("What is the weight of Beep?")
    beep_weight = float(input())

    print("What is the weight of Bop?")
    bop_weight = float(input())

    print("What would you like to calculate (sum or average)?")
    calculate = input()

    if calculate == "sum":
        sum = sum_weights(beep_weight, bop_weight)
        print(f"The sum of Beep and Bop's weight is: {sum:.0f}.")
    else:
        avg = calc_avg_weight(beep_weight, bop_weight)
        print(f"The average of Beep and Bop's weight is: {avg:.0f}.")


