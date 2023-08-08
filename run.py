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