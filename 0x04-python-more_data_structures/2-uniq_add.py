#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = 0
    for idx in set(my_list):
        uniq += idx
    return (uniq)
