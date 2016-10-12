#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/9/28 18:08
# __Author__  : Kira
# __File__    : combine_multipule_map_to_single_map.py

from collections import ChainMap
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(c['x'])
print(c['z'])
c['z'] = 10
c['w'] = 40
del c['z']
print(a)
