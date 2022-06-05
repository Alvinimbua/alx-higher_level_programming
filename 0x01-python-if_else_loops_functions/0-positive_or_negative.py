#!/usr/bin/python3
import random
number = random.randint(-10, 10)

def positive_zero_or_negative(a):

    if n == 0:
        return f"{a:d} is zero"
    elif n > 1:
        return f"{a:d} is positive"
    else:
        return f"{a:d} is negative"

    if __name __ == "__main__":
        print(positive_zero_or_negative(number))
