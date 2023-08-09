# Guitar Stock Database
This is a Python application that manages the stock for a warehouse of guitars. It allows you to search for guitars by make or model, add stock to the database, remove stock from the database, and update the prices of guitars.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Bugs](#bugs)
- [Data Structure](#data-structure)

## Features
- Search for guitars by make or model.
- Add new guitars to the database or update stock quantity.
- Remove guitars from the database or update stock quantity.
- Update the prices of guitars in the database.

## Getting Started
1. Go here: https://guitar-stock-db-plynch-pp3-e3da63835834.herokuapp.com/ 
2. Hit the run program button
3. Follow the on-screen instructions to interact with the Guitar Stock Database.
4. The main menu allows you to choose various options:
- Press 0 to search by make.
- Press 1 to search by model.
- Press 2 to add stock to the database.
- Press 3 to remove stock from the database.
- Press 4 to update the price of a guitar in the database.
5. Options 0 and 1 are pretty straight forward, say you have 2 electric guitar types in stock e.g. Fender Telecaster & Fender Stratocaster. Option 0 means that if you type Fender into it it will give you all the data attached to Fender guitars in the database. Option 1 means that if you type Telecaster into the database then it will give you only the data related to the Telecasters.
6. Option 2. Allows the user to add stock into the database by inputting the make & model. The program will then ask how many of this item they wish to add to the stock. In the event that the item has never existed in the database before the program will inform the user that the item is the first of it's kind in the database and ask if the user would like to add the item to the database. After inputting y you will prompted to return to the main menu. If you would like to add a stock amount to the new item you use option 2 and re-enter the make and model. Then the amount of stock you wished to add.
7. Option 3 is like option 2 but in reverse. If something is sold or returned or maybe by human error has entered the wrong amount into the database via option 2 then you can remove it. Enter the make and model if it exists in the database it will tell you how many are in stock and input for a number to remove
8. Option 4 is a way for users to update price. If an item has just been added to the database then this option should be executed immediately after. otherwise items will appear to be free on the database. Again we are prompted to input a make and then a model and if the item exists in the database then you can change it.

## Bugs
- Bug #1: Fixed an issue where the application would bunch up the JSON data when writing to `db.json`, making the database hard to read.
- Bug #2: Fixed a bug in the `search_guitar_by_make` function where the application did not find guitars with multiple words in the make. Removed spaces to match the entered make and the make in the database without spaces.
- Bug #3: Fixed a bug in the `add_stock_to_database` function where adding stock without all keys (make, model, price, and stock quantity) caused a crash. Now the application checks for the presence of all keys before allowing stock addition.
- Bug #4: Fixed a bug in the `remove_stock_from_database` function where removing stock without all keys (make and model) caused a crash. Now the application checks for the presence of all keys before allowing stock removal.
- Bug #5: Fixed a bug in the `add_stock_to_database` function where entering "2" to cancel did not return to the main menu. Now, entering "2" works as expected and goes back to the main menu.
- Bug #6: Fixed a bug in the `update_price_in_database` function where entering a new price did not update the price of the guitar in the database. The price is now correctly updated.


Thank you for taking the time to read this & run my project. Hip Hip Hooray!!!

## Data Structure
The guitar database is stored in a JSON file named `db.json`. The data is structured as follows:
```json
[
{
 "make": "Fender",
 "model": "Telecaster",
 "price": "1700",
 "stock quantity": "12"
},
{
 "make": "Fender",
 "model": "Stratocaster",
 "price": "1750",
 "stock quantity": "10"
},
{
 "make": "Gibson",
 "model": "Les Paul",
 "price": "1200",
 "stock quantity": "1"
}
]


Thank you for taking the time to read this & run my project. Hip Hip Hooray!!!