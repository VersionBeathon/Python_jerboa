#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/9/28 17:37
# __Author__  : Kira
# __File__    : transform_and_reduce_data_same_time.py

nums = [1, 2, 3, 4, 5]
s = map(lambda x: x * x, nums)
s = [i for i in s]
print(s)
z = ('ACME', 50, 123.45)
print(','.join(str(x) for x in z))
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
s = sum(x * x for x in nums)
print(s)
max_shares = max(portfolio, key=lambda s: s['shares'])
print(max_shares)