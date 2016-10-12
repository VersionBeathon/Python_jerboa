#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/9/27 17:21
# __Author__  : Kira
# __File__    : map_names_to_sequece_elements.py

from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub.joined)
print(sub.addr)
print(len(sub))
addr, joined = sub
print(addr)
print(joined)

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)
print(s)
s=s._replace(shares=75)
print(s)