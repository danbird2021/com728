import sqlite3

def retrieve_bot():
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM bots")
    single_row = cursor.fetchone()
    db.close()
    print(single_row)

def run():
    retrieve_bot()

# Determine if main file is being executed.
if __name__ == "__main__":
    run()