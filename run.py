import os
import json


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_guitar(guitar):
    for key, value in guitar.items():
        print(f"{key.capitalize()}: {value}")


def load_data_from_json(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def save_data_to_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def search_guitar_by_make(guitars):
    clear_screen()
    print("Please type the make of guitar you want to find:")
    make_to_find = input("Make: ").strip().lower().replace(" ", "")

    found_guitars = [guitar for guitar in guitars if guitar["make"].lower().replace(" ", "") == make_to_find]

    if found_guitars:
        clear_screen()
        print(f"Guitars with Make: {make_to_find.capitalize()}")
        for guitar in found_guitars:
            display_guitar(guitar)
            print("------------------------------------------------")
    else:
        print("No guitars found with that make.")
    input("Press Enter to return to the main menu.")
    else:
        print("No guitars found with that make.")
    input("Press Enter to return to the main menu.")


def search_guitar_by_model(guitars):
    clear_screen()
    print("Please type the model of guitar you want to find:")
    model_to_find = input("Model: ").strip().lower().replace(" ", "")

    found_guitars = [guitar for guitar in guitars if guitar["model"].lower().replace(" ", "") == model_to_find]

    if found_guitars:
        clear_screen()
        print(f"Guitars with Model: {model_to_find.capitalize()}")
        for guitar in found_guitars:
            display_guitar(guitar)
            print("------------------------------------------------")
    else:
        print("No guitars found with that model.")
    input("Press Enter to return to the main menu.")


def add_stock_to_database(guitars):
    while True:
        clear_screen()
        print("What item would you like to add to the stock?")
        make = input("Make: ").capitalize()
        model = input("Model: ").capitalize()

        if make == '2' or model == '2':
            return

        existing_guitar = next((guitar for guitar in guitars if guitar["make"] == make and guitar["model"] == model), None)
        if existing_guitar:
            print("Guitar found in the database.")
            print(f"Current stock quantity: {existing_guitar['stock quantity']}")
            quantity_to_add = int(input("How many of this item would you like to add: "))
            clear_screen()
            print(f"You have entered {quantity_to_add} of this item.")
            confirm = input("Are you sure you want to add this amount? (y/n): ")
            if confirm.lower() == "y":
                current_stock = int(existing_guitar["stock quantity"])
                new_stock = current_stock + quantity_to_add
                existing_guitar["stock quantity"] = str(new_stock)
                print(f"{quantity_to_add} added to stock.")
            else:
                print("Operation canceled. Stock not added.")
                input("Press Enter to return to the main menu.")
                return
        else:
            print("Guitar not found in the database.")
            add_new_guitar = input("Do you want to add a new guitar to the database? (y/n): ")
            if add_new_guitar.lower() == 'y':
                new_guitar = {
                    "make": make,
                    "model": model,
                    "price": "0",
                    "stock quantity": "0"
                }
                guitars.append(new_guitar)
                print("New guitar added to stock.")
            else:
                print("Operation canceled. Stock not added.")
                input("Press Enter to return to the main menu.")
                return

        input("Press Enter to return to the main menu.")
        return

def remove_stock_from_database(guitars):
    while True:
        clear_screen()
        print("What item would you like to remove from the stock?")
        make_to_remove = input("Make: ").strip().lower().replace(" ", "")
        model_to_remove = input("Model: ").strip().lower().replace(" ", "")

        if make_to_remove == '2' or model_to_remove == '2':
            return

        found_guitars = [guitar for guitar in guitars if guitar["make"].lower().replace(" ", "") == make_to_remove and guitar["model"].lower().replace(" ", "") == model_to_remove]
        if not found_guitars:
            print("No guitars found with that make and model.")
            input("Press Enter to return to the main menu.")
            return

        guitar_to_remove = found_guitars[0]
        display_guitar(guitar_to_remove)

        print(f"Current stock quantity: {guitar_to_remove['stock quantity']}")
        quantity_to_remove = int(input("How many of this item would you like to remove: "))
        clear_screen()
        print(f"You have entered {quantity_to_remove} of this item.")
        confirm = input("Are you sure you want to remove this amount? (y/n): ")
        if confirm.lower() == "y":
            current_stock = int(guitar_to_remove["stock quantity"])
            new_stock = current_stock - quantity_to_remove
            guitar_to_remove["stock quantity"] = str(new_stock)
            print(f"{quantity_to_remove} removed from stock.")
        else:
            print("Operation canceled. Stock not removed.")
            input("Press Enter to return to the main menu.")
            return

        input("Press Enter to return to the main menu.")
        return


def update_price_in_database(guitars):
    clear_screen()
    print("What item's price would you like to update?")
    make_to_update = input("Make: ").capitalize()
    model_to_update = input("Model: ").capitalize()

    guitar_to_update = next((guitar for guitar in guitars if guitar["make"] == make_to_update and guitar["model"] == model_to_update), None)
    if guitar_to_update:
        clear_screen()
        display_guitar(guitar_to_update)

        new_price = input("Enter the new price for this item: ")
        try:
            new_price_float = float(new_price)
            if new_price_float < 0:
                raise ValueError("Price must be zero or above")
            
            guitar_to_update["price"] = new_price_float
            print("Price updated successfully.")
        except ValueError:
            print("Invalid price. Please enter a valid non-negative number.")
        
        input("Press Enter to return to the main menu.")
    else:
        print("Guitar not found in the database.")
        input("Press Enter to return to the main menu.")


def main():
    db_file_path = 'db.json'
    guitars = load_data_from_json(db_file_path)

    while True:
        clear_screen()
        print("Welcome to the Guitar Stock database.\n\n\n")
        print("Press 0 to search by make")
        print("Press 1 to search by model")
        print("Press 2 to add stock to the database")
        print("Press 3 to remove stock")
        print("Press 4 to update price")
        choice = input("Choose option to continue: ")

        if choice == "0":
            search_guitar_by_make(guitars)
        elif choice == "1":
            search_guitar_by_model(guitars)
        elif choice == "2":
            add_stock_to_database(guitars)
        elif choice == "3":
            remove_stock_from_database(guitars)
        elif choice == "4":
            update_price_in_database(guitars)
        else:
            print("Please select a valid option.")
            input("Press Enter to continue.")

        save_data_to_json(db_file_path, guitars)


main()