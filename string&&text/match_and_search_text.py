#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/12 11:17
# __Author__  : Kira
# __File__    : match_and_search_text.py

import re
text1 = '11/27/2012'
text2 = 'nov 27, 2012'
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
if re.match(r'[a-z]*\B', text2):
    print('yes')

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
m = datepat.match(text1)
print(m.group(0))
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))
for m in datepat.finditer(text):
    print(m.group())
print('\n')
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
month, day, year = m.groups()
print(datepat.findall(text))
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))