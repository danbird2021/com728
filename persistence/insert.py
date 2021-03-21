import sqlite3

def get_bot_from_user():
    bot = []

    print("Please enter the name of the bot:")
    bot_name = input().strip().lower()
    bot.append(bot_name)

    print("Please enter the maximum speed of the bot:")
    max_speed = int(input())
    bot.append(max_speed)

    print("Please enter the maximum strength of the bot:")
    max_strength = int(input())
    bot.append(max_strength)

    print("Please enter the date of manufacture:")
    created_date = input().strip()
    bot.append(created_date)

    print("Please enter manufacturer id:")
    manufac_id = int(input())
    bot.append(manufac_id)


    print("Please enter home planet id of bot:")
    planet_id = int(input())
    bot.append(planet_id)

    print("Please enter film franchise id of bot:")
    franchise_id = int(input())
    bot.append(franchise_id)

    return bot

def insert_bot_in_db(bot):

    db = sqlite3.connect("bots.db")
    cursor = db.cursor()

    sql = "INSERT INTO bots (name, max_speed, max_strength, date_created, manufacturer_id, home_planet_id, film_franchise_id) " \
          f"VALUES ('{bot[0]}', {bot[1]}, {bot[2]}, '{bot[3]}', {bot[4]}, {bot[5]}, {bot[6]})"

    print(sql)
    cursor.execute(sql)
    last_record_id = cursor.lastrowid
    db.commit()
    db.close()
    return last_record_id

def run():

    record_id = insert_bot_in_db(get_bot_from_user())
    print("The record has been added to the database.")
    print(f"The record id is {record_id}.")


# Determine if main file is being executed.
if __name__ == "__main__":
    run()