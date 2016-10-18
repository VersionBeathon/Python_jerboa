#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/17 16:35
# __Author__  : Kira
# __File__    : binary_octal_hexadecimal_int.py

x = 1234
# 转换成二进制
print(bin(x))
print(format(x, 'b'))
# 转换成八进制
print(oct(x))
print(format(x, 'o'))
# 转换成十六进制
print(hex(x))
print(format(x, 'x'))

print(int('4d2', 16))
print(int('10011010010', 2))
