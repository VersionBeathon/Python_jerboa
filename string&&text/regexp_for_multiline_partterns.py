#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/12 15:24
# __Author__  : Kira
# __File__    : regexp_for_multiline_partterns.py

import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
     multiline comment */
    '''
print(comment.findall(text1))
print(comment.findall(text2))

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))