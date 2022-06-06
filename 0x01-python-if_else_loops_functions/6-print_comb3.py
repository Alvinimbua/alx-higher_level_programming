#!/usr/bin/python3

for x in range(10):
    for y in range(x + 1, 10):
        if x != y:
            i = f"{x}{y}"
            if i != '89':
                print("{}".format(i), end=", ")
            else:
                print(i)
