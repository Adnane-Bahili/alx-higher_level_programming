#!/usr/bin/python3
for d in range(9):
    for dc in range(d+1, 10):
        if (d == 8 and dc == 9):
            print("{}{}".format(d, dc))
            break
        print("{}{}".format(d, dc), end=', ')
