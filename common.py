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
