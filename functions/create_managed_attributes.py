#!/user/bin/env python
# _*_coding:utf-8_*_
# @Time   :2017/1/20 13:25
# @Author :Kira
# @Software：PyCharm
import math


class Person:

    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError('Can`t delete attribute')


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

'''
c.area  属性
c.area() 方法
'''