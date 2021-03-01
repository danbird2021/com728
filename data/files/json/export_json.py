# A program to retrieve data from a json file and store it to a new json file.
# Import json module
import json

def read(file_path):
    print("Reading...")
    """
    Display to the user reading message, then open file_path as file using passed variable file_path.
    Using json module load method, load file data into variable data.
    Display to user done message and return variable data.
    """
    with open(file_path) as file:
        data = json.load(file)

    print("Done!")

    return data

def save(file_path, save_data):
    print("Exporting...")
    """
    Display to user exporting message.
    Using passed variable 'file_path' as 'file_path' open as file in write mode.
    json module dump method will be used next to store the data passed from save_data to file 
    at file_path designated with a space indent of 4.
    Display to user done message.
    """
    with open(file_path, "w") as file:
        json.dump(save_data, file, indent=4)

    print("Done!")


def run():
    """
    Call function read and pass file_path and place return value in data 'json_data'.
    Next call save function and pass json_data variable contents and file_path to location where
    contents are to be saved.
    """
    json_data = read("robocity.json")
    save("exported.json", json_data)

# Determine if main file is being executed.
if __name__ == "__main__":
  run()

