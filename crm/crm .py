# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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
    table = data_manager.get_table_from_file("crm/customers.csv")
    title_list = ["ID", "Name", "Email", "Subscriber 1(yes) 0(no)"]
    options = ["Show table",
               "Add item",
               "Remove item",
               "Update item",
               "get_longest_name_id",
               "get_subscribed_emails"]
    while True:
        ui.print_menu("Customer relationship management", options, "Return to main menu")
        try:
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == "1":
                show_table(table)
            elif option == "2":
                add(table)
            elif option == "3":
                id_ = ui.get_inputs(["Please enter the ID of the item to remove: "], "Remove item")[0]
                remove(table, id_)
            elif option == "4":
                id_ = ui.get_inputs(["Please enter the ID of the item to update: "], "Update item")[0]
                update(table, id_)
            elif option == "5":
                get_longest_name_id(data_manager.get_table_from_file("crm/customers.csv"))
            elif option == "6":
                get_subscribed_emails(data_manager.get_table_from_file("crm/customers.csv"))
            elif option == "0":
                return
            else:
                raise KeyError("There is no such option.")
        except KeyError as err:
            ui.print_error_message(err)


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["ID", "Name", "Email", "Subscriber 1(yes) 0(no)"]
    ui.print_table(table, title_list)
    return


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title_list = ["Name", "Email", "Subscriber 1(yes) 0(no)"]
    type_list = [str, str, int]
    new_input = common.input_func(title_list, type_list, table, "Add store item: \n")
    if new_input != "exit":
        new_input.insert(0, common.generate_random(table))
        table.append(new_input)
    data_manager.write_table_to_file("crm/customers.csv", table)
    start_module()
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    id_list = []
    for i in table:
        id_list.append(i[0])
    while id_ not in id_list:
        ui.print_error_message('The given ID is not in table!')
        id_ = ui.get_inputs(['Please enter the ID of the item to remove: '], '')[0]
    for i, item in enumerate(id_list):
        if item == id_:
            del table[i]
    data_manager.write_table_to_file("crm/customers.csv", table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    id_list = []
    for i in table:
        id_list.append(i[0])
    while id_ not in id_list:
        ui.print_error_message('The given ID is not in table!')
        id_ = ui.get_inputs(['Please enter the ID of the item to update: '], '')[0]

    title_list = ["Name", "Email", "Subscriber 1(yes) 0(no)"]
    type_list = [str, str, int]
    get_update = ui.get_inputs(title_list, "Add data for update:")
    corrected_record = common.check_type(get_update, title_list, type_list)

    for id_index, item in enumerate(id_list):
        if item == id_:
            for record_index, item in enumerate(corrected_record):
                table[id_index][record_index + 1] = item
    data_manager.write_table_to_file("crm/customers.csv", table)
    return table


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table):
    table = data_manager.get_table_from_file("crm/customers.csv")
    lenght = 0
    longest_id_list = []
    for row in table:
        if len(row[1]) > lenght:
            lenght = len(row[1])
    for row in table:
        if lenght == int(len(row[1])):
            longest_id_list.append(row[0])
    temp_list = []
    for counter in range(0, len(longest_id_list)):
        abc = ""
        for row in longest_id_list:
            if row.lower() > abc.lower() and row not in temp_list:
                abc = row
        temp_list.append(abc)
    temp_list.reverse()
    ui.print_result(temp_list, "The id(s) of the costumer(s) with the longest name:\n ")
    return temp_list


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    table = data_manager.get_table_from_file("crm/customers.csv")
    subscribers = []
    separator = ";"
    for row in table:
        if row[3] == str(1):
            subscribers.append(row[2] + separator + row[1])
        else:
            continue
    ui.print_result(subscribers, "The list of the costumers who subscribed:\n ")
    return subscribers
