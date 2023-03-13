#!/usr/bin/python3
# a function that replaces an element of a list at a specific position
def replace_in_list(my_list, idx, element):
    # If idx is negative, the function should not modify anything,
    # and returns the original list
    list_len = len(my_list)
    if idx < 0:
        return my_list
    # If idx is out of range (> of number of element in my_list),
    # the function should not modify anything, and returns the original list
    elif idx > list_len:
        return my_list
    else:
        my_list[idx] = element
        return my_list
