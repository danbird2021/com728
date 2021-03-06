# A program to load the Titanic data set using the csv module.
import csv

records = []
headings = []

def load_data(file_path):
    print("Loading data...")
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
  

    """)
    menu_choice = int(input())
    return menu_choice

def run():
    load_data("titanic.csv")
    print(f"Successfully loaded {len(records)} records.")

    selected_option = display_menu()
    print(f"You have selected option: {selected_option}")


# Determine if main file being executed.
if __name__ == "__main__":
    run()
