#!/usr/bin/python3
for n in range(99):
    hexarg = n % 16
    if hexarg == 10:
        hexarg = 'a'
    elif hexarg == 11:
        hexarg = 'b'
    elif hexarg == 12:
        hexarg = 'c'
    elif hexarg == 13:
        hexarg = 'd'
    elif hexarg == 14:
        hexarg = 'e'
    elif hexarg == 15:
        hexarg = 'f'
    h = int(n / 16)
    if n < 16:
        h = ''
    print("{} = 0x{}{}".format(n, h, hexarg))
