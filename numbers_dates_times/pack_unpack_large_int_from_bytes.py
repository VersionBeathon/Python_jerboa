#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Time__    : 16/10/17 16:52
# __Author__  : Kira
# __File__    : pack_unpack_large_int_from_bytes.py
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))
x = 0x01020304
print(x.to_bytes(4, 'big'))
print(x.to_bytes(4, 'little'))