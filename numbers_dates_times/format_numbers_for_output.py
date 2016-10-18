#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/17 16:22
# __Author__  : Kira
# __File__    : format_numbers_for_output.py
x = 1234.235346
print(format(x, '0.2f'))
print(format(x, '>10.1f'))
print(format(x, '^10.1f'))
print(format(x, ','))
print(format(x, '0,.1f'))
print(format(x, 'e'))
print(format(x, '0.2e'))
print('The value is {:0,.2f}'.format(x))