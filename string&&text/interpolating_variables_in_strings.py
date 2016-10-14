#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/14 14:12
# __Author__  : Kira
# __File__    : interpolating_variables_in_strings.py

s = '{name} has {n} message.'
print(s.format(name='Guido', n=37))

name = 'Guido'
n = 37
print(s.format_map(vars()))

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


a = Info('Guido', 37)
print(s.format_map(vars(a)))
