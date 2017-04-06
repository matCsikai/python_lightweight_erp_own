# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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
               "Add item",
               "Remove item",
               "Update item",
               "Year with the highest profit",
               "Average profit by item"]
    while True:
        ui.print_menu("Accounting manager", options, "Return to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(data_manager.get_table_from_file("accounting/items.csv"))
        elif option == "2":
            add(data_manager.get_table_from_file("accounting/items.csv"))
        elif option == "3":
            remove(data_manager.get_table_from_file("accounting/items.csv"))
        elif option == "4":
            id_ = ui.get_inputs(["Please enter the ID of the item to update: "], "Update item")[0]
            update(data_manager.get_table_from_file("accounting/items.csv"), id_)
        elif option == "5":
            which_year_max(data_manager.get_table_from_file("accounting/items.csv"))
        elif option == "6":
            year = ui.get_inputs(["Please enter the year: "], "")[0]
            avg_amount(data_manager.get_table_from_file("accounting/items.csv"), year)
        elif option == "0":
            return
        else:
            raise KeyError("There is no such option.")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["ID", "Month", "Day", "Year", "Income/Outcom", "Amount(dollar)"]
    ui.print_table(table, title_list)
    return

    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title_list = ["Month", "Day", "Year", "Income(in)/Outcome(out)", "Amount(dollar)"]
    type_list = [int, int, int, str, int]
    new_input = common.input_func(title_list, type_list, table, "Add store item: \n")
    valid_answers = ["in", "out"]
    while new_input[3] not in valid_answers:
        new_input[3] = str(ui.get_inputs(["Please add in or out! "], "")[0])
    if new_input != "exit":
        new_input.insert(0, common.generate_random(table))
        table.append(new_input)
    data_manager.write_table_to_file("accounting/items.csv", table)
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
                data_manager.write_table_to_file("accounting/items.csv", table)
                found_input = True
        if found_input is False:
            ui.print_error_message("\nNot souch ID\n")
            remove(table)
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
        options = ["Month", "Day", "Year", "Income(in)/Outcome(out)", "Amount(dollar)"]
        ui.print_menu("", options, "Return to Accounting menu")
        while True:
            try:
                inputs = ui.get_inputs(["Please enter the number of the data to update or 0 to return to Account menu: "],"")
                option = inputs[0]
                if option == "1":
                    type_list = [int]
                    month_update = ui.get_inputs(['Month '], "Add new month: ")
                    corrected_record = common.check_type(month_update, ['Month'], type_list)
                    for i, id in enumerate(id_list):
                        if id == id_:
                            table[i][1] = corrected_record[0]
                            data_manager.write_table_to_file("accounting/items.csv", table)
                            ui.print_result(table[i], 'Record updated: ')
                elif option == "2":
                    type_list = [int]
                    day_update = ui.get_inputs(['Day '], "Add new day: ")
                    corrected_record = common.check_type(day_update, ['Day'], type_list)
                    for i, id in enumerate(id_list):
                        if id == id_:
                            table[i][2] = corrected_record[0]
                            data_manager.write_table_to_file("accounting/items.csv", table)
                            ui.print_result(table[i], 'Record updated: ')
                elif option == "3":
                    type_list = [int]
                    year_update = ui.get_inputs(['Year '], "Add new year: ")
                    corrected_record = common.check_type(year_update, ['Year'], type_list)
                    for i, id in enumerate(id_list):
                        if id == id_:
                            table[i][3] = corrected_record[0]
                            data_manager.write_table_to_file("accounting/items.csv", table)
                            ui.print_result(table[i], 'Record updated: ')
                elif option == "4":
                    type_list = [str]
                    income_update = ui.get_inputs(['Income(in)/Outcome(out) '], "Add new Income/Outcome: ")
                    corrected_record = common.check_type(income_update, ['Income(in)/Outcome(out)'], type_list)
                    for i, id in enumerate(id_list):
                        if id == id_:
                            table[i][4] = corrected_record[0]
                            data_manager.write_table_to_file("accounting/items.csv", table)
                            ui.print_result(table[i], 'Record updated: ')
                elif option == "5":
                    type_list = [int]
                    amount_update = ui.get_inputs(['Amount(dollar) '], 'Amount(dollar): ')
                    corrected_record = common.check_type(amount_update, ['Amount(dollar)'], type_list)
                    for i, id in enumerate(id_list):
                        if id == id_:
                            table[i][5] = corrected_record[0]
                            data_manager.write_table_to_file("accounting/items.csv", table)
                            ui.print_result(table[i], 'Record updated: ')
                elif option == "0":
                    return
                else:
                    raise KeyError("There is no such option.")
            except KeyError as err:
                ui.print_error_message(err) 
    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    result_list = []
    for row in table:
        if row[3] in result_list:
            for i in range(len(result_list)+1):
                if result_list[i] == row[3]:
                    if row[4] == "in":
                        result_list[i+1] += int(row[5])
                    else:
                        result_list[i+1] -= int(row[5])
                    break
        else:
            result_list.append(row[3])
            if row[4] == "in":
                result_list.append(int(row[5]))
            else:
                result_list.append(int(row[5])*-1)
    max_profit = 0
    for i in range(1, len(result_list), 2):
        if result_list[i] > max_profit:
            max_profit = result_list[i]
            year = result_list[i-1]
    ui.print_result(year, "The year of the highest profit: ")
    return int(year)


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    counter = 0
    income = 0
    for row in table:
        if row[3] == year:
            counter += 1
            if row[4] == "in":
                income += int(row[5])
            else:
                income -= int(row[5])
    if counter == 0:
        ui.print_error_message("There was no profit in {} year".format(year))
        return None
    ui.print_result(income/counter, "The average profit in {}:".format(year))
    return income/counter
