#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/12 17:12
# __Author__  : Kira
# __File__    : aligning_text_strings.py
text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
print(text.rjust(20,'-'))
print(text.center(20, '*'))
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
print('{:=^20}'.format(text))
x = 1.2345
print('{:>10}'.format(x))
print('{:^10.2f}'.format(x))