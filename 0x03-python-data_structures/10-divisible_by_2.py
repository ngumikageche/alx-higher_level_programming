#!/usr/bin/python3
# a function that finds all multiples of 2 in a list.
def divisible_by_2(my_list=[]):
    list_len = len(my_list)
    new_list = []
    for i in range(list_len):
        if my_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
