#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nums = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            nums += 1
        except (ValueError, TypeError):
            continue
    print("")
    return nums
