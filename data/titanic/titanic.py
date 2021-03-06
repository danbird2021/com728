# A program to load the Titanic data set using the csv module.
import csv

records = []
headings = []

def load_data(file_path):
    print("Loading data...", end="")
    with open(file_path) as file:
        csv_reader = csv.reader(file)

        headings.append(next(csv_reader))

        for values in csv_reader:
            records.append(values)

    print("Done!")

def display_menu():
    print("""
Please select one of the following options:
[1] Display the names of all passengers
[2] Display the number of passengers that survived
[3] Display the number of passengers per gender
[4] Display the number of passengers per age group
[5] Display the number of survivors per age group  

    """)
    menu_choice = int(input())
    return menu_choice

def display_passenger_names():
    print(f"The names of the passengers are...\n")
    passenger_name = ""
    for record in records:
        passenger_name = record[3]
        print(f"{passenger_name}")

def display_num_survivors():
    num_survived = 0

    for record in records:
        survival_status = int(record[1])
        if survival_status == 1:
            num_survived += 1

    print(f"{num_survived} passengers survived")

def display_passengers_per_gender():
    females = 0
    males = 0

    for record in records:
        gender = record[4]
        if gender == "male":
            males += 1
        elif gender == "female":
            females += 1

    print(f"females: {females}, males: {males}")

def display_passengers_per_age_group():

    children = 0
    adults = 0
    elderly = 0

    for record in records:
        if record[5] != "":
            age = int(float(record[5]))
            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1
    print(f"children: {children}, adults: {adults}, elderly: {elderly}")

def display_survivors_per_age_group():
    children_survived = 0
    adults_survived = 0
    elderly_survived = 0
    no_age_survived = 0

    children = 0
    adults = 0
    elderly = 0
    no_age = 0

    for record in records:
        survival_status = int(record[1])
        if record[5] == "":
            no_age += 1
            if survival_status == 1:
                no_age_survived += 1
        elif record[5] != "":
            age = int(float(record[5]))
            if age < 18:
                children += 1
                if survival_status == 1:
                    children_survived += 1
            elif age < 65:
                adults += 1
                if survival_status == 1:
                    adults_survived += 1
            else:
                elderly += 1
                if survival_status == 1:
                    elderly_survived += 1
    print(f"children: {children_survived}/{children}, adults: {adults_survived}/{adults}, elderly: {elderly_survived}/{elderly}, no age given: {no_age_survived}/{no_age}")



def run():
    load_data("titanic.csv")
    print(f"Successfully loaded {len(records)} records.")

    selected_option = display_menu()
    print(f"You have selected option: {selected_option}\n")
    if selected_option == 1:
        display_passenger_names()
    elif selected_option == 2:
        display_num_survivors()
    elif selected_option == 3:
        display_passengers_per_gender()
    elif selected_option == 4:
        display_passengers_per_age_group()
    elif selected_option == 5:
        display_survivors_per_age_group()
    else:
        print("Error! Option not recognised!")
#    print(headings)
#    print(records)
# Determine if main file being executed.
if __name__ == "__main__":
    run()
