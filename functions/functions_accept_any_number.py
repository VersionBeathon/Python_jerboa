#!/user/bin/env python
# _*_coding:utf-8_*_
# @Time   :2017/1/10 13:52
# @Author :Kira
# @Software：PyCharm


def anyargs(*args, **kwargs):
    print(args)
    print(kwargs)

# 理解位置参数与关键词参数
# *位置参数，**关键词参数，分别以元组，字典传递进去
anyargs(1111, 1111, a=1, b=2, c=3)