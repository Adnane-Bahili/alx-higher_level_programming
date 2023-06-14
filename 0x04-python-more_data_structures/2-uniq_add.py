#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for u in set(my_list):
        result += u
    return (result)
