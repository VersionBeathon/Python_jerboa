#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/12 14:20
# __Author__  : Kira
# __File__    : specify_regexp_for_shortest_match.py
import re
str_pat = re.compile(r'\"(.*?)\"')
text = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text))