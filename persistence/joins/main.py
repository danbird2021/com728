import database

def menu():
    print(f"""Please select one of the following options:
    
[1] Display stock levels
[2] Display suppliers
[3] Display supplier locations
[4] Display missing suppliers \n""")

    response = int(input("Your selection:"))

    return response

def run():

    menu_choice = menu()

    if menu_choice == 1:
        database.display_products_with_stock_levels()
    elif menu_choice == 2:
        database.display_product_supplier()
    elif menu_choice == 3:
        database.display_product_supplier_locations()
    elif menu_choice == 4:
        database.display_products_missing_suppliers()



# Determine if main file is being executed.
if __name__ == "__main__":
    run()
