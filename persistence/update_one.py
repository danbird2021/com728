import sqlite3

def get_bot_id_from_user():
    print("Please enter a bot id:")
    bot_id = int(input())
    return bot_id

def display_bot_from_db(bot_id):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    sql = f"SELECT * FROM bots WHERE id = {bot_id}"
    cursor.execute(sql)
    single_row = cursor.fetchone()
    db.close()
    print(f"Current bot details are as follows: \n"
          f"id: {single_row[0]}, name: {single_row[1]}, max_speed: {single_row[2]}, max_strength: {single_row[3]}"
          f", date_created: {single_row[4]}, manufacturer: {single_row[5]}, home_planet_id: {single_row[6]}, film_franchise_id: {single_row[7]}")

def get_bot_details_from_user():
    print("\nWhat would you like to change?")
    field = input().strip().lower()
    print(f"\nWhat is the new value for {field}?")
    new_value = input().strip().lower()
    return [field, new_value]

def update_bot_in_db(bot_id, bot_details):
    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    if bot_details[0] == 'name' or 'date created':
        sql = f"UPDATE bots SET {bot_details[0]} = '{bot_details[1]}' WHERE id = {bot_id}"
    else:
        sql = f"UPDATE bots SET {bot_details[0]} = {bot_details[1]} WHERE id = {bot_id}"
    cursor.execute(sql)
    db.commit()
    db.close()

def run():
    bot_id = get_bot_id_from_user()
    display_bot_from_db(bot_id)
    bot_details = get_bot_details_from_user()
    update_bot_in_db(bot_id, bot_details)
    print("\nThe record has been updated.")

# Determine if main file is being executed.
if __name__ == "__main__":
    run()