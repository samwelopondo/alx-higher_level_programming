#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None

    for i in range(len(my_list)):
        for j in range(len(my_list) - 1):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return (my_list[len(my_list) - 1])
