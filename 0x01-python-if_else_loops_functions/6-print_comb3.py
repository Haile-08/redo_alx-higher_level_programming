#!/usr/bin/python3
n = 1
for i in range(0, 9):
    for j in range(n, 10):
        print("{:d}{:d}".format(i, j), end=", ")
    n = n + 1
