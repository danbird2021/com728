# A program to export user data  and append to the end of a CSV file.


def export(file_path, num_bots):
    """
    Retrieve file path and number of bots to append to file.
    Retrieve from user: ID, Name and Paint for each number of bots required,
    append these details to the end of file.
    Display to user completion message.
    """
    with open(file_path, "a") as file:
        for b in range(num_bots):
            print("Please enter the ID of the bot:")
            id = int(input())
            print("Please enter a name for the bot:")
            name = input()
            print("Please enter the paint for the bot:")
            paint = input()

            file.write(f"\n{id},{name},{paint}")
        print("Exporting...", end="")
    print("Done!")

def run():
    """
    Call export function and pass parameters: file path and number of bots required.
    """
    export("exported_bots.csv", 2)

# Determine if main file being executed.
if __name__ == "__main__":
    run()