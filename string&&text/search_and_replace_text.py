#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/12 11:36
# __Author__  : Kira
# __File__    : search_and_replace_text.py
import re
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2', text)
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
