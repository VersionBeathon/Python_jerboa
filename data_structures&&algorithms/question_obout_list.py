# _*_ coding:utf-8 _*_
#!/usr/bin/env python3
# 骚的不行的数据处理方式
import heapq
p = (4, 5)
x, y = p
print(p, '\n', x, y)
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, share, price, date = data
print(name)
print(share)
print(price)
print(date)
name, share, price, (year, mon, day) = data
print(year)
print(mon)
s = 'Hello'
a, b, c, d, e = s
print(a)
# 丢掉某些特定值
_, shares, price, _ = data
print(shares)
print(price)
grade = [11, 23, 42, 67, 123, 43]
# '*' 的用法


def drop_first_last(grades):
    first, *middle, last = grades
    return middle

print(drop_first_last(grade))

record = ('Dave', 'dave@example.com', '77712737172983', '780234643256')
name, email, *phone_numbers = record
print(phone_numbers)

*trailing, current = [10, 23, 455, 12354, 674, 1235676]
print (trailing)
# heap采用堆排序，sort采用归并排序
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
print(heap)
heapq.heapify(heap)
# 迭代方法

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
