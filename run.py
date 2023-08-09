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
    """Searches for guitar by make"""
    clear_screen()
    make_to_find = input("Please type the make of guitar you want to find: ").capitalize()
    found_guitars = [guitar for guitar in guitars if guitar["make"] == make_to_find]
    if found_guitars:
        for guitar in found_guitars:
            display_guitar(guitar)
    else:
        print("No guitars found with that make.")
    input("Press Enter to return to the main menu.")


def search_guitar_by_model(guitars):
    """Searches for guitar by model"""
    clear_screen()
    model_to_find = input("Please type the model of guitar you want to find: ").capitalize()
    found_guitars = [guitar for guitar in guitars if guitar["model"] == model_to_find]
    if found_guitars:
        for guitar in found_guitars:
            display_guitar(guitar)
    else:
        print("No guitars found with that model.")
    input("Press Enter to return to the main menu.")


def add_stock_to_database(guitars):
    clear_screen()
    new_guitar = {}
    print("What item would you like to add to the stock?")
    for key in ["make", "model", "price", "stock quantity"]:
        value = input(f"{capitalize_first_letter(key)}: ").capitalize()
        new_guitar[key] = value

    if all(value for value in new_guitar.values()):
        clear_screen()
        print(f"Current stock quantity: {new_guitar['stock quantity']}")
        quantity_to_add = int(input("How many of this item would you like to add: "))
        clear_screen()
        print(f"You have entered {quantity_to_add} of this item.")
        confirm = input("Are you sure you want to add this amount? (y/n): ")
        if confirm.lower() == "y":
            current_stock = int(new_guitar["stock quantity"])
            new_stock = current_stock + quantity_to_add
            new_guitar["stock quantity"] = str(new_stock)
            print(f"{quantity_to_add} added to stock.")
        else:
            print("Item not added to stock.")
    else:
        print("All fields must be filled.")
    
    input("Press Enter to return to the main menu.")

def remove_stock_from_database(guitars):
    clear_screen()
    print("What item would you like to remove from the stock?")
    make_to_remove = input("Make: ").capitalize()
    model_to_remove = input("Model: ").capitalize()
    found_guitars = [guitar for guitar in guitars if guitar["make"] == make_to_remove and guitar["model"] == model_to_remove]
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
        print("Item not removed from stock.")
    
    input("Press Enter to return to the main menu.")


def main():
    guitars = []  # List to store guitar dictionaries

    while True:
        clear_screen()
        print("Welcome to the Guitar Stock database.\n\n\n")
        print("Press 0 to search by make")
        print("Press 1 to search by model")
        print("Press 2 to add stock to the database")
        print("Press 3 to remove stock")
        choice = input("Choose option to continue: ")

        if choice == "0":
            search_guitar_by_make(guitars)
        elif choice == "1":
            search_guitar_by_model(guitars)
        elif choice == "2":
            add_stock_to_database(guitars)
        elif choice == "3":
            remove_stock_from_database(guitars)
        else:
            print("Please select a valid option.")
            input("Press Enter to continue.")


main()