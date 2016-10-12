#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/9/29 14:12
# __Author__  : Kira
# __File__    : startwith&&endwith.py

import os
filenames = os.listdir(u'/Users/songmingyang/Documents/workspace/deal_data/Python2.7/spy_eleme/')
names = [name for name in filenames if name.endswith(('py', 'dat'))]
print(names)

