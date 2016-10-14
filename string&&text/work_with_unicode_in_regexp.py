#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/12 16:31
# __Author__  : Kira
# __File__    : work_with_unicode_in_regexp.py
import re
num = re.compile('\d+')
r = num.match('123')
print(r.string)
print(num.match('\u0661\u0662\u0663').string)
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
print(arabic)
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
pat.match(s)
print(pat.match(s.upper()))
print(s.upper())
