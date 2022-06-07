#!/usr/bin/python3

def replace_in_list(my_list, abc, element):
    if abc > (len(my_list) - 1) or abc < 0:
        return my_list
    else:
        my_list[abc] = element
        return my_list
