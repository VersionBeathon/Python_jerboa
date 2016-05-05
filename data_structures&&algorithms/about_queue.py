# _*_ coding:utf-8 _*_
'''
实现一个队列，它能够以给定的优先级来对元素排序，
且每次pop操作时都会返回优先级最高的那个元素
'''
import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 将priority self._index item 组成个元组进入堆 - 代表倒序的意思
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        # format 格式化字符串
        # {!r} {!s} 取得%r和%s的效果
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
