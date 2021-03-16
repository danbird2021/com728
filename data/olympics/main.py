import csv
import process
import tui


def read_data(file_path):
    tui.started(file_path)
    data = []
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for values in csv_reader:
            data.append(values)
    tui.completed()
    return data


def run():
    athlete_data = read_data("athlete_events.csv")

    while True:
        selection = tui.menu()
        if selection == "years":
            process.list_years(athlete_data)
        elif selection == "tally":
            process.tally_medals(athlete_data)
        elif selection == "team":
            process.tally_team_medals(athlete_data)
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run()
