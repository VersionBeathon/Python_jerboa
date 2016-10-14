#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/14 14:52
# __Author__  : Kira
# __File__    : reformat_text_to_fixed_number_columns.py
import textwrap
import os
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40, initial_indent ='    '))
print(s.split(' '))

# 获取终端屏幕尺寸
print(os.get_terminal_size().columns)
