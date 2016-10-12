#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/12 10:47
# __Author__  : Kira
# __File__    : match_strings_with_shell_wildcard.py

from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foofuck.txt', '*.txt'))
names = ['date.csv', 'data.csv', 'data1.csv', 'data2.csv']
print([name for name in names if fnmatch(name, '*.csv')])
# fnmatch 使用底层系统的大小写敏感规则(不同系统不同)

print(fnmatchcase('foo.txt', '*.TXT'))
# fnmatchcase 对大小写就敏感

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])
