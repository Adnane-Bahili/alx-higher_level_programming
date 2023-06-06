#!/usr/bin/python3
for lcm in range(97, 123):
    if chr(lcm) == 'q' or chr(lcm) == 'e':
        continue
    print("{}".format(chr(lcm)), end='')
