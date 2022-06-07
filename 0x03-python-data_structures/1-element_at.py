#!/usr/bin/python3

def element_at(my_list, abc):
    if abc > (len(my_list) - 1) or abc < 0:
        return None
    else:
        return my_list[abc]
