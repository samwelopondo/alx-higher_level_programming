#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = []
    total = 0
    for i in range(len(my_list)):
        if my_list[i] not in result:
            result.append(my_list[i])
            total += my_list[i]
    return total
