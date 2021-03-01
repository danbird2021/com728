# A program to retrieve and display content from a JSON file.
import json

def run(file_path):
    """
    Retrieve file path and open as file.
    Using json module load content of file in variable data.
    Display City name and population, followed by the stats, speed
    and strength for each bot.
    """
    with open(file_path) as file:
        data = json.load(file)

        print(f"City Name: {data['city']}")
        print(f"Population: {data['population']}")

        for b in data['bots']:
            print(f"{b['name']} has the following stats: {b['stats']}")

# Determine if main file is being executed.
if __name__ == "__main__":
  run("robocity.json")