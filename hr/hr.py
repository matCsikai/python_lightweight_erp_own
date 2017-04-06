# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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
    table = data_manager.get_table_from_file("hr/persons.csv")
    title_list = ["ID", "Name", "Year of birth"]
    options = ["Show table",
               "Add item",
               "Remove item",
               "Update item",
               "Get oldest person",
               "Get persons closest to average"]
    while True:
        ui.print_menu("Human resources manager", options, "Return to main menu")
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
                get_oldest_person(table)
            elif option == "6":
                get_persons_closest_to_average(table)
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
    title_list = ["ID", "Name", "Year of birth"]
    ui.print_table(table, title_list)
    return


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title_list = ['Name ', 'Year of birth ']
    type_list = [str, int]
    get_record = ui.get_inputs(title_list, "Add new record:")
    corrected_record = common.check_type(get_record, title_list, type_list)
    new_record = []
    new_record.append(common.generate_random(table))
    new_record += corrected_record
    table.append(new_record)
    data_manager.write_table_to_file("hr/persons.csv", table)
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
    data_manager.write_table_to_file("hr/persons.csv", table)
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
    

    while True:
        options = ['Name ', 'Year of birth ']
        ui.print_menu("", options, "Return to HR menu")
        while True:
            try:
                inputs = ui.get_inputs(["Please enter the number of the data to update or 0 to return to HR menu: "], "")
                option = inputs[0]
                if option == "1":
                    type_list = [str]
                    name_update = ui.get_inputs(['Name '], "Add new name: ")
                    corrected_record = common.check_type(name_update, ['Name'], type_list)
                    for i, id in enumerate(id_list):
                        if id == id_:
                            table[i][1] = corrected_record[0]
                            data_manager.write_table_to_file("hr/persons.csv", table)
                            ui.print_result(table[i], 'Record updated: ')
                elif option == "2":
                    type_list = [int]
                    year_update = ui.get_inputs(['Year '], "Add new year of birth: ")
                    corrected_record = common.check_type(year_update, ['Year'], type_list)
                    for i, id in enumerate(id_list):
                        if id == id_:
                            table[i][2] = corrected_record[0]
                            data_manager.write_table_to_file("hr/persons.csv", table)
                            ui.print_result(table[i], 'Record updated: ')
                elif option == "0":
                    return
                else:
                    raise KeyError("There is no such option.")
            except KeyError as err:
                ui.print_error_message(err)


    '''
    title_list = ['Name ', 'Year of birth ']
    type_list = [str, int]
    get_update = ui.get_inputs(title_list, "Add data for update:")
    corrected_record = common.check_type(get_update, title_list, type_list)

    for id_index, item in enumerate(id_list):
        if item == id_:
            for record_index, item in enumerate(corrected_record):
                table[id_index][record_index + 1] = item
    data_manager.write_table_to_file("hr/persons.csv", table)
    '''

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    age = []
    for i in table:
        age.append(2017-int(i[2]))
    oldest_age = 0
    oldests = []
    for i in age:
        if i > oldest_age:
            oldest_age = i
    for index, item in enumerate(age):
        if item == oldest_age:
            oldests.append(table[index][1])
    ui.print_result(oldests, 'The oldest person(s):')
    return oldests


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    age = 0
    ages = []
    number_of_persons = 0
    for i in table:
        age += (2017-int(i[2]))
        ages.append(2017-int(i[2]))
        number_of_persons += 1
    average_age = age/number_of_persons
    closests = []
    close = 100
    for i in ages:
        if abs(i-average_age) < close:
            close = abs(i-average_age)
            result = i
    for index, item in enumerate(ages):
        if item == result:
            closests.append(table[index][1])
    ui.print_result(closests, 'The person(s) closest to average age:')
    return closests
