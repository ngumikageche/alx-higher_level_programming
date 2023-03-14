#!/usr/bin/python3
# a function that finds the biggest integer of a list.
def max_integer(my_list=[]):
    list_len = len(my_list)
    if list_len == 0:
        return None
    else:
        my_list.sort()
        return my_list[-1]
