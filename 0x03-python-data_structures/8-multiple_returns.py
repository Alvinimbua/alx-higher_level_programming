#!/usr/bin/python3

def multiple_returns(sentence):
    a = sentence
    if a == "":
        return (0, None)
    return (len(a), a[0])
