#!/usr/bin/python3

def new_in_list(my_list, abc, element):
    new_list = my_list[:]
    if abc > (len(new_list) - 1) or abc < 0:
        return new_list
    else:
        new_list[abc] = element
        return 
