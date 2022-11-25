#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = list(map(float, input().split()))
    rn1 = float(input("range 1: "))
    rn2 = float(input("range 2: "))
    max_ = a[0]
    pos = 0
    max_ = max(a)
    b = []
    for ind, val in enumerate(a):
        if val > 0:
            pos += val
        else:
            break
    for i, item in enumerate(a):
        if not((abs(item) > rn1) and (abs(item) < rn2)):
            b.append(item)
    while len(b) < len(a):
        b.append(0)
    print(b)
    print('\nmaximum is: ', max_, '\nsum is: ', pos)
