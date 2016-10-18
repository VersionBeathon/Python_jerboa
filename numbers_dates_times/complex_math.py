#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/17 17:12
# __Author__  : Kira
# __File__    : complex_math.py
a = complex(2, 4)
print(a)
b = 3 - 5j
print(b)
print(a.real)
print(a.imag)
print(a.conjugate())
print(a + b)
print(a * b)
# 设z1=a+bi，z2=c+di(a、b、c、d∈R)是任意两个复数，那么它们的积(a+bi)(c+di)=(ac-bd)+(bc+ad)i