#!/usr/bin/python3

def no_c(my_string):
    for a in my_string:
        if a in "Cc":
            my_string = my_string.split(a)
            my_string = "".join(my_string)
    return my_string 
