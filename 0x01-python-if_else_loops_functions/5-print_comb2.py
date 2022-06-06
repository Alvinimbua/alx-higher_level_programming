#!/usr/bin/python3

for d in range(100):
    if d != 99:
        print("{:02d}".format(d), end=", ")
    else:
        print(d)
