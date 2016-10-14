#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/12 16:17
# __Author__  : Kira
# __File__    : normalize_unicode_text_to_regexp.py
import unicodedata
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(ascii(t1))
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)
print(ascii(t3))
s = '\ufb01'
print(s)
print(unicodedata.normalize('NFD', s))
print(unicodedata.normalize('NFKD', s))
print(unicodedata.normalize('NFKC', s))
print(unicodedata.normalize('NFKD', s) == unicodedata.normalize('NFKC', s))

t1 = unicodedata.normalize('NFD', s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))