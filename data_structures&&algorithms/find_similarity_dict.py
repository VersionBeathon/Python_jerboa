#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/9/18 15:43
# __Author__  : Kira
# __File__    : find_similarity_dict.py


a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())

c = {key:a[key] for key in a.keys() - {'z', 'y'}}
print(c)
print([i for i in a.items()])
