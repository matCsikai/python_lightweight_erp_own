

# This function needs to print outputs like this:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table
def print_table(table, title_list):

    # your code
    columns_max_length = [0] * len(title_list)
    table.insert(0, title_list)
    for row in table:
        counter_columns = 0
        while counter_columns <= len(row) - 1:
            if len(row[counter_columns]) > columns_max_length[counter_columns]:
                if len(row[counter_columns]) % 2 != 0:
                    columns_max_length[counter_columns] = int(len(row[counter_columns]) + 1)
                else:
                    columns_max_length[counter_columns] = int(len(row[counter_columns]))
            counter_columns += 1
    table_lenght = 0
    for lenghts in columns_max_length:
        table_lenght = table_lenght + lenghts
    for row in table:
        print("-" * (table_lenght + len(columns_max_length) + 1))
        counter_columns = 0
        while counter_columns <= len(row) - 1:
            space = " " * (columns_max_length[counter_columns] - len(row[counter_columns]))
            print("|", space, row[counter_columns], end="", sep="")
            counter_columns += 1
        print("|")
    print("-" * (table_lenght + len(columns_max_length) + 1))
    del table[0]






# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):

    # your code

    pass


# This function needs to generate outputs like this:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):
    #print('Main menu:\n(1) Store manager\n(2) Human resources manager\n(3) Inventory manager\n(4) Accounting manager\n (5) Selling manager\n (6) Customer relationship management (CRM)\n (0) Exit program')
    print(title)
    for index, menu_objects in enumerate(list_options, 1):
        print('({0}) {1}'.format(index, menu_objects))
    #print(enumerate(list_options))
    print('(0)', exit_message)
    # your code

    pass


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):
    inputs = []
    print(title)
    inputs.append(input(list_labels))
    # your code

    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):

    # your code

    pass
