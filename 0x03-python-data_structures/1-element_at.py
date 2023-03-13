#!/usr/bin/python3
# a function that retrieves an element from a list like in C
def element_at(my_list, idx):
    list_len = len(my_list)
    if idx < 0:# If idx is negative, the function should return None
        return None
    elif idx > list_len:# If idx is out of range (> of number of element in my_list), the function should return None
        return None
    else:
        return my_list.pop(idx)
