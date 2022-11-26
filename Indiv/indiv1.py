#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if len(A) != 10:
        print("size isn't right", file=sys.stderr)
        exit(1)
    s = 0
    for ind, val in enumerate(A):
        if (abs(val) > 3) and (abs(val) < 8):
            s += val
    print(s)

