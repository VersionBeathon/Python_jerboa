#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/9/29 11:39
# __Author__  : Kira
# __File__    : splite_string_on_multiple_delimiters.py
import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[:,\s]\s*', line))
fields = re.split(r'(:|,|\s)\s*', line)
print(fields)
print(re.split(r'(?:,|;|\s)\s*', line))