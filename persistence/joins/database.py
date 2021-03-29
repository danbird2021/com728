import sqlite3

def display_products_with_stock_levels():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM product NATURAL JOIN stock")
    all_rows = cursor.fetchall()
    num_of_products = 0
    db.close()


    print(f"There are {len(all_rows)} products in the catalogue.")
    print(f"The stock level for each product is as follows:\n")
    for row in all_rows:
        print(f"""Product: {row[1]}
Description: {row[2]}
Stock level: {row[3]}\n""")
        
    

