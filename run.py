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
    make_to_find = input("Please type the make of guitar you want to find: ").capitalize()
    found_guitars = [guitar for guitar in guitars if guitar["make"] == make_to_find]
    if found_guitars:
        for guitar in found_guitars:
            display_guitar(guitar)
    else:
        print("No guitars found with that make.")
    input("Press Enter to return to the main menu.")


def search_guitar_by_model(guitars):
    clear_screen()
    model_to_find = input("Please type the model of guitar you want to find: ").capitalize()
    found_guitars = [guitar for guitar in guitars if guitar["model"] == model_to_find]
    if found_guitars:
        for guitar in found_guitars:
            display_guitar(guitar)
    else:
        print("No guitars found with that model.")
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