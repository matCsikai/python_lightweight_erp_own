# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


# importing everything you need
import os
import sys
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():
    options = ["Show table",
               "Add store item",
               "Remove item",
               "Update item",
               "What is the id of the item that sold for the lowest price ?",
               "Average by manufacturer"]
    while True:
        ui.print_menu("Sales:", options, "Return to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(data_manager.get_table_from_file("selling/sellings.csv"))
        elif option == "2":
            add(data_manager.get_table_from_file("selling/sellings.csv"))
        elif option == "3":
            remove(data_manager.get_table_from_file("selling/sellings.csv"))
        elif option == "4":
            update(data_manager.get_table_from_file("selling/sellings.csv"))
        elif option == "5":
            get_lowest_price_item_id(data_manager.get_table_from_file("selling/sellings.csv"))
        elif option == "6":
            get_items_sold_between(data_manager.get_table_from_file("selling/sellings.csv"))
        elif option == "0":
            return
        else:
            raise KeyError("There is no such option.")
        pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "title", "price", "month", "day", "year"]
    ui.print_table(table, title_list)
    return


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title_list = ["title", "price", "month", "day", "year"]
    type_list = [str, int, int, int, int]
    new_input = common.input_func(title_list, type_list, table, "Add store item: \n")
    if new_input != "exit":
        if int(new_input[2]) <= 12 and int(new_input[3]) <= 31:
            new_input.insert(0, common.generate_random(table))
            table.append(new_input)
        else:
            print("\nWrong input!\n")
            return table
    data_manager.write_table_to_file("selling/sellings.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table):
    title_list = ["ID"]
    type_list = [str]
    new_input = common.input_func(title_list, type_list, table, "\nRemove item. \n")
    found_input = False
    if new_input != "exit":
        for row in table:
            if str(row[0]) == str(new_input[0]):
                table.remove(row)
                data_manager.write_table_to_file("selling/sellings.csv", table)
                found_input = True
        if found_input is False:
            print("\nNot souch ID\n")
            remove(table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table):
    title_list = ["ID"]
    type_list = [str]
    new_input = common.input_func(title_list, type_list, table, "\nUpdate item. \n")
    found_input = False
    if new_input != "exit":
        title_list = ["title", "price", "month", "day", "year"]
        type_list = [str, int, int, int, int]
        update_input = common.input_func(title_list, type_list, table, "Update item: \n")
        row_counter = 0
        for row in table:
            if str(row[0]) == str(new_input[0]):
                table[row_counter] = update_input
                table[row_counter].insert(0, str(new_input[0]))
                data_manager.write_table_to_file("selling/sellings.csv", table)
                found_input = True
            row_counter += 1
        if found_input is False:
            print("\nNot souch ID\n")
            remove(table)
    return table


# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order
def get_lowest_price_item_id(table):
    lowest_price = int(table[1][2])
    for prices in table:
        if int(lowest_price) > int(prices[2]):
            lowest_price = int(prices[2])
    list_of_lowest_prices = []
    for prices in table:
        if int(lowest_price) == int(prices[2]):
            list_of_lowest_prices.append(prices[0])
    temp_list = []
    for counter in range(0, len(list_of_lowest_prices)):
        abc = ""
        for row in list_of_lowest_prices:
            if row > abc and row not in temp_list:
                abc = row
        temp_list.append(abc)
    ui.print_result(temp_list, "\nid of the item that sold for the lowest price:\n")
    return table


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    
    # your code

    pass
