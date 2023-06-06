#!/usr/bin/python3
def uppercase(str):
    for c in str:
        other = ord(c)
        if other < 97 or other > 122:
            a = c
        else:
            a = chr(other - 32)
        print("{}".format(a), end="")
    print("")
