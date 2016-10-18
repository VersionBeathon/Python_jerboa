#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/17 13:55
# __Author__  : Kira
# __File__    : perform_text_operations.py
import re
data = b'hello world'
print(data[0:5])
print(data.startswith(b'hello'))
print(data.split())
a = data.replace(b'hello', b'hello curel')
print(a)
data = bytearray(b'hello world')
print(data[0:5])
print(data.split())

data = b'FOO:BAR,SPAM'
print(re.split(b'[:,]',data))

