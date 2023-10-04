#!/usr/bin/python3
def print_last_digit(number):
    result = ""
    last_digit = abs(number) % 10
    result += "{}".format(last_digit)
    print(result, end='')
    return (result)
