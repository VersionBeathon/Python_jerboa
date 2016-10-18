#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/17 15:58
# __Author__  : Kira
# __File__    : accurate_decimal_calculations.py
from decimal import Decimal, getcontext
import math
getcontext().prec = 4
a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)
c = Decimal(4.2)
d = Decimal(2.1)
print(c + d)
nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))
print(math.fsum(nums))