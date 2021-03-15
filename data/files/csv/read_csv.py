# A program to display the content of a CSV file.
# Import csv module.
import csv


def run(file_path):
    """
    Retrieve file path and open as file.
    Read CSV file using CSV reader from csv module.
    Display all the headings from file under Headings first
    and then all values from file under values.
    """
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(f"Headings:\n{headings}")
        print("Values:")
        for values in csv_reader:
            print(values[1])


# Determine if main file being executed.
if __name__ == "__main__":
    run("bots.csv")
