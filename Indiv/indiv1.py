#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    if len(A) != 10:
        print("size isn't right", file=sys.stderr)
        exit(1)
    s = sum(i for i in A if (abs(i) > 3) and (abs(i) < 8))
    print(s)

