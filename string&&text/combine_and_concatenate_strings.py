#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/13 15:27
# __Author__  : Kira
# __File__    : combine_and_concatenate_strings.py

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))
a = '1'
b = '2'
c = '5'
print(a + ':' + b + ':' + c)
print(":".join([a, b, c]))
print(a, b ,c , sep=':')