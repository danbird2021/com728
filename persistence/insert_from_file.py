import csv
import sqlite3

def read_data_file(file_path):
    data = []
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        for values in csv_reader:
            data.append(values)

    return data

def insert_to_db(data):

    db = sqlite3.connect("bots.db")
    cursor = db.cursor()
    print("Inserting data into the database...")
    sql = "INSERT INTO bots (name, max_speed, max_strength, date_created, manufacturer_id, home_planet_id, film_franchise_id) " \
          f"VALUES "
    record_count = 0
    for d in range (len(data)):
        if d == (len(data)-1):
            sql += f"('{data[d][0]}', {data[d][1]}, {data[d][2]}, '{data[d][3]}', {data[d][4]}, {data[d][5]}, {data[d][6]});"
            record_count += 1
        else:
            sql += f"('{data[d][0]}', {data[d][1]}, {data[d][2]}, '{data[d][3]}', {data[d][4]}, {data[d][5]}, {data[d][6]}),"
            record_count += 1
    cursor.execute(sql)
    db.commit()
    db.close()
    print(f"Done! {record_count} records inserted.")
def run():
    print("Please enter the file path:")
    file_path = input().strip().lower()
    data = read_data_file(file_path)
    insert_to_db(data)

if __name__ == "__main__":
    run()

