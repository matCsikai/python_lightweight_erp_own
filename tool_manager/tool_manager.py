# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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
    table = data_manager.get_table_from_file("tool_manager/tools.csv")
    title_list = ["ID", "Name", "Manifacturer", "Purchase date", "Durability"]
    options = ["Show table",
               "Add item",
               "Remove item",
               "Update item",
               "get_available_tools",
               "get_average_durability_by_manufacturers"]
    while True:
        ui.print_menu("Inventory manager", options, "Return to main menu")
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
                get_available_tools(data_manager.get_table_from_file("tool_manager/tools.csv"))
            elif option == "6":
                get_average_durability_by_manufacturers(data_manager.get_table_from_file("tool_manager/tools.csv"))
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
    title_list = ["ID", "Name", "Manifacturer", "Purchase date", "Durability"]
    ui.print_table(table, title_list)
    return


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title_list = ["Name", "Manifacturer", "Purchase date", "Durability"]
    type_list = [str, str, int, int]
    new_input = common.input_func(title_list, type_list, table, "Add store item: \n")
    if new_input != "exit":
        new_input.insert(0, common.generate_random(table))
        table.append(new_input)
    data_manager.write_table_to_file("tool_manager/tools.csv", table)
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
    data_manager.write_table_to_file("tool_manager/tools.csv", table)
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

    title_list = ["Name", "Manifacturer", "Purchase date", "Durability"]
    type_list = [str, str, int, int]
    get_update = ui.get_inputs(title_list, "Add data for update: ")
    corrected_record = common.check_type(get_update, title_list, type_list)

    for id_index, item in enumerate(id_list):
        if item == id_:
            for record_index, item in enumerate(corrected_record):
                table[id_index][record_index + 1] = item
    data_manager.write_table_to_file("tool_manager/tools.csv", table)
    return table


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_tools(table):
    table = data_manager.get_table_from_file("tool_manager/tools.csv")
    final_list = []
    year_now = 2017
    for row in table:
        if (year_now - int(row[3])) <= int(row[4]):
            final_list.append(row)
        else:
            continue
    ui.print_result(final_list, "This items has not exceeded their durability yet:\n")
    return final_list


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):
    table = data_manager.get_table_from_file("tool_manager/tools.csv")
    result_list = []
    for row in table:
        if row[2] in result_list:
            for i in range(len(result_list)+1):
                if result_list[i] == row[2]:
                    result_list[i+1] += int(row[4])
                    result_list[i+2] += 1
                    break
        else:
            result_list.append(row[2])
            result_list.append(int(row[4]))
            result_list.append(1)
    final_result = {}
    for item in range(0, len(result_list), 3):
        final_result[result_list[item]] = result_list[item + 1] / result_list[item + 2]
    ui.print_result(final_result, "The average durabilities are: ")
    return final_result
