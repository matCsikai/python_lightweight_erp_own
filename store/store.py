# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


# importing everything you need
import os
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
               "Counts by manufacturers",
               "Average by manufacturer"]
    while True:
        ui.print_menu("Store department", options, "Return to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(data_manager.get_table_from_file("store/games.csv"))
        elif option == "2":
            add(data_manager.get_table_from_file("store/games.csv"))
        elif option == "3":
            remove(data_manager.get_table_from_file("store/games.csv"))
        elif option == "4":
            update(data_manager.get_table_from_file("store/games.csv"))
        elif option == "5":
            get_counts_by_manufacturers(data_manager.get_table_from_file("store/games.csv"))
        elif option == "6":
            get_average_by_manufacturer(data_manager.get_table_from_file("store/games.csv"))
        elif option == "0":
            return
        else:
            raise KeyError("There is no such option.")
        pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["ID", "Name", "Manufacturer", "price (dollar)", "in_stock"]
    ui.print_table(table, title_list)
    return


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title_list = ["Name", "Manufacturer", "price (dollar)", "in_stock"]
    type_list = [str, str, int, int]
    new_input = common.input_func(title_list, type_list, table, "Add store item: \n")
    if new_input != "exit":
        new_input.insert(0, common.generate_random(table))
        table.append(new_input)
    data_manager.write_table_to_file("store/games.csv", table)
    start_module()
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
                data_manager.write_table_to_file("store/games.csv", table)
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
        title_list = ["Name", "Manufacturer", "price (dollar)", "in_stock"]
        type_list = [str, str, int, int]
        update_input = common.input_func(title_list, type_list, table, "Update store item: \n")
        row_counter = 0
        for row in table:
            if str(row[0]) == str(new_input[0]):
                table[row_counter] = update_input
                table[row_counter].insert(0, str(new_input[0]))
                data_manager.write_table_to_file("store/games.csv", table)
                found_input = True
            row_counter += 1
        if found_input is False:
            print("\nNot souch ID\n")
            remove(table)
    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    manufacturer_dict = {}
    for row in table:
        if row[2] in manufacturer_dict:
            manufacturer_dict[row[2]] += 1
        else:
            manufacturer_dict[row[2]] = 1
    ui.print_result(manufacturer_dict, "\nDifferent kinds of game are available of each manufacturer:\n")
    return table


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table):
    title_list = ["Manufacturer"]
    type_list = [str]
    list_of_uniqe_manufacturer = []
    counter = 1
    for manufacturer in table:
        if manufacturer[2] not in list_of_uniqe_manufacturer:
            list_of_uniqe_manufacturer.append(manufacturer[2])
            print(counter, manufacturer[2])
            counter += 1
    new_input = common.input_func(title_list, type_list, table, "\nAverage by manufacturer \n")
    list_of_stock = []
    all_amount = 0
    if new_input != "exit":
        for stock in table:
            if stock[2] == list_of_uniqe_manufacturer[int(new_input[0]) - 1]:
                list_of_stock.append(stock[4])
                all_amount += int(stock[4])
    average_amount = all_amount / len(list_of_stock)
    ui.print_result(average_amount, "\nAverage amount of games in stock of a given manufacturer:\n")
    return table
