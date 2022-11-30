#!/usr/bin/python3
for n in range(97, 97+26):
    j = chr(n)
    if j != 'q' and j != 'e':
        print("{}".format(j), end="")
