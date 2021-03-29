import database

def menu():
    print(f"""Please select one of the following options:
[1] Display stock levels\n""")

    response = int(input("Your selection:"))

    return response

def run():

    menu_choice = menu()

    if menu_choice == 1:
        database.display_products_with_stock_levels()

# Determine if main file is being executed.
if __name__ == "__main__":
    run()
