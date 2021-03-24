import sqlite3

def retrieve_bots():
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM bots")
    all_rows = cursor.fetchall()
    print("\nAll bots in the system:\n")
    for row in all_rows:
        print(row)

    db.close()

def run():
    retrieve_bots()

# Determine if main file is being executed.
if __name__ == "__main__":
    run()