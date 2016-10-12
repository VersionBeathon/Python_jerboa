#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/9/27 14:55
# __Author__  : Kira
# __File__    : sorted_by_key_word.py

from pprint import pprint
from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
pprint(rows_by_fname)
print('\n')
pprint(rows_by_uid)
rows_by_lfname = sorted(rows, key=itemgetter('fname', 'lname'))
print('\n')
pprint(rows_by_lfname)

rows_by_fname = sorted(rows, key= lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lfname'], r['fname']))

min(rows, key=itemgetter('uid'))
max(rows, key=itemgetter('uid'))