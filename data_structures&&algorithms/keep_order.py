#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/9/18 16:42
# __Author__  : Kira
# __File__    : keep_order.py


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_dict(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)