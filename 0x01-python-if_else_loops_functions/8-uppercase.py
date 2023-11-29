#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        uni = ord(str[i])
        if uni >= 97 and uni <= 122:
            uni = uni -32
        print("{}".format(chr(uni)), end = '')
    print()
