#!/usr/bin/python3
# a function that deletes the item at a specific position in a list.
def delete_at(my_list=[], idx=0):
    len_list = len(my_list)
    if idx >= 0 or idx < len_list:
        del my_list[idx]
    return my_list
