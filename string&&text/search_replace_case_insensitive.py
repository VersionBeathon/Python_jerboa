#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/12 12:01
# __Author__  : Kira
# __File__    : search_replace_case_insensitive.py

import re

text = 'UPPER PYTHON, lower python, Mixed Python'


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
print(text)
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))
print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))