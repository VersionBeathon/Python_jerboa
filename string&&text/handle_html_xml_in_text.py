#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/14 15:13
# __Author__  : Kira
# __File__    : handle_html_xml_in_text.py
import html
s = 'Elements are written as "<tag>text</tag>".'
print(s)
print(html.escape(s))
print(html.escape(s, quote=False))