#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = list(map(float, input().split()))
    rn1 = float(input("range 1: "))
    rn2 = float(input("range 2: "))
    pos = 0
    max_ = max(a)
    for i in a:
        if i > 0:
            pos += i
        else:
            break
    c = [i for i in a if not((abs(i) > rn1) and (abs(i) < rn2))]
    while len(c) < len(a):
        c.append(0)
    print(c)
    print('\nmaximum is: ', max_, '\nsum is: ', pos)


