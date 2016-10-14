#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/12 16:45
# __Author__  : Kira
# __File__    : strip_unwanted_characters.py
import re
s = ' hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.replace(' ', ''))
print(re.sub('\s+', '', s))
with open(filename) as f:
    lines = (line.strip() for line in f)
    [print(line) for line in lines]