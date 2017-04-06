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

    # you code
    options = ["Show table",
               "Add store item",
               "Remove item",
               "Update item",
               "Counts by manufacturers",
               "Average by manufacturer"]
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
        accounting.start_module()
    elif option == "5":
        selling.start_module()
    elif option == "6":
        crm.start_module()
    elif option == "0":
        main.main()
    else:
        raise KeyError("There is no such option.")
    pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["ID", "Name", "Manufacturer", "price (dollar)", "in_stock"]
    # your code
    ui.print_table(table, title_list)
    start_module()


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title_list = ["Name", "Manufacturer", "price (dollar)", "in_stock"]
    type_list = [str, str, int, int]
    new_input = common.input_func(title_list, type_list, table, "Add store item: \n")
    if new_input != "exit":
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
    new_input = common.input_func(title_list, type_list, table, "Remove item \n")
    if new_input != "exit":
        for ?????
        table.remove(new_input)
    data_manager.write_table_to_file("store/games.csv", table)
    start_module()
    return table
    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):

    # your code

    pass


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):

    # your code

    pass
