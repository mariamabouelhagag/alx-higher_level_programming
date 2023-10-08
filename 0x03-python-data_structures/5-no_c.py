#!/usr/bin/python3
def no_c(my_string):
    without_c = str.maketrans('', '', 'cC')
    new_string = my_string.translate(without_c)
    return new_string
