import sqlite3

def display_products_with_stock_levels():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    cursor.execute("SELECT product.name, product.description, stock.quantity FROM product NATURAL JOIN stock")
    all_rows = cursor.fetchall()
    num_of_products = 0
    db.close()


    print(f"\nThere are {len(all_rows)} products in the catalogue.")
    print(f"The stock level for each product is as follows:\n")
    for row in all_rows:
        print(f"""Product: {row[0]}
Description: {row[1]}
Stock level: {row[2]}\n""")


def display_product_supplier():
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    cursor.execute("SELECT product.name, supplier.name  FROM product INNER JOIN supplier ON product.supplier_id = supplier.id")
    all_rows = cursor.fetchall()
    db.close()

    for row in all_rows:
        print(f"Product: {row[0]}, Supplier: {row[1]}")
        
    

