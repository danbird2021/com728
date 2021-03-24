import sqlite3

def retrieve_bots(num_bots = None):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM bots")

    if num_bots == None:
        all_rows = cursor.fetchall()
        print("\nAll bots in the system:\n")
    else:
        all_rows = cursor.fetchmany(num_bots)

    for row in all_rows:
        print(row)

    db.close()

def run():
    print("First 3 bots in the system:")
    retrieve_bots(3)

# Determine if main file is being executed.
if __name__ == "__main__":
    run()