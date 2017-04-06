# implement commonly used functions here

import random

'''abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)


def generate_random(table):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    punctuation = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    generated = random.choice(lower_case) + random.choice(upper_case) + random.choice(digits) + random.choice(punctuation) + random.choice(lower_case) + random.choice(upper_case) + random.choice(digits) + random.choice(punctuation)
    if generated not in table:
        return generated
    else:
        generate_random(table)


def input_func(title_list, type_list, table, title):
    new_row = []
    print(title)
    for expected_type, question in enumerate(title_list):
        input_type = False
        while input_type is False:
            new_item = (input("Please add {}?: ".format(question)))
            if new_item.lower() == "exit":
                return "exit"
            if type_list[expected_type] != str:
                try:
                    new_item = type_list[expected_type](new_item)
                except:
                    continue
                else:
                    new_row.append(str(new_item))
                    input_type = True
            else:
                new_row.append(str(new_item))
                input_type = True
    return new_row