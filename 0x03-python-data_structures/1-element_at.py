#!/usr/bin/python3
# a function that retrieves an element from a list like in C
def element_at(my_list, idx):
    list_len = len(my_list)
    if idx < 0:  # If idx is negative, the function should return None
        return None
    # If idx is out of range (> of number of element in my_list),
    # the function should return None
    elif idx > list_len - 1:
        return None
    else:
        return my_list.pop(idx)
