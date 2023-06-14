#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    avg = 0
    size = 0

    for tpl in my_list:
        avg += (tpl[0] * tpl[1])
        size += tpl[1]
    return (avg / size)
