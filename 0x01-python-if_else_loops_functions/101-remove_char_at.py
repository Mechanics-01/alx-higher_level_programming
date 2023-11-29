#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0:
        return str

    count = 0
    str_cpy = ""
    for element in str:
        if count == n:
            count += 1
            continue
        str_cpy += str[count]
        count += 1
    return
