# A program to extract and display specific content of a CSV file using the csv module.
# Import csv module.
import csv


def run(file_path):
    """
    Retrieve file path and open as file.
    Read CSV file using CSV reader from csv module.
    Retrieve all the headings from file and ignore then
    display all values from column 1 of CSV file.
    """
    with open(file_path) as file:
        print("Extracting...")
        names = ""
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for values in csv_reader:
            names += (f"{values[1]}\n")
        print(f"Done! The extracted names are as follows:\n{names}")



# Determine if main file being executed.
if __name__ == "__main__":
    run("bots.csv")
