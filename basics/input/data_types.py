#Basic BMI calculator using different data types
def run():
    print("What is your name human?")
    name = input()

    print("How old are you (in years)?")
    age = int(input())

    print("How tall are you (in meters)?")
    height = float(input())

    print("How much do you weigh (in kilograms)?")
    weight = float(input())

    bmi = weight/(height ** 2)

    print(f"{name} you are {age} years old and your bmi is {bmi:.2f}.")

    # if statement to determine category from bmi calculation
    if  bmi < 18.5:
        category = "underweight"
    elif bmi >= 18.5 and  bmi <= 24.9:
        category = "normal weight"
    elif bmi  >= 25 and bmi <= 29.9:
        category = "overweight"
    elif bmi >= 30:
        category = "obese"

    # display category to user
    print(f"You are classed as {category}.")
