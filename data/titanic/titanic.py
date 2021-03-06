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


def run():
    load_data("titanic.csv")
    print(f"Successfully loaded {len(records)} records.")

# Determine if main file being executed.
if __name__ == "__main__":
    run()
