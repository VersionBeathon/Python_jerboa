#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/9/27 16:38
# __Author__  : Kira
# __File__    : filter_list_item.py

import math
from itertools import compress
mylist = [1, 3 , 4, -5, -6, -7, 2, 8, -8, -9]

# 列表推导
print([x for x in mylist if x > 0])
# 生成器表达式
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)

values = ['1', '2', '3', '-', ',' , 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)

print([math.sqrt(x) for x in mylist if x > 0])
clip_neg = [n if n > 0 else 0 for n in mylist]
clip_pos = [n if n < 0 else 0 for n in mylist]

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n > 5 for n in counts]
print(list(compress(addresses, more5)))