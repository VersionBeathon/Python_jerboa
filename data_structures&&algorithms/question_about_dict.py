# _*_ coding:utf-8 _*_
# 将键（key）映射到多个值的字典（一键多值字典[multidict]）
from collections import defaultdict
from collections import OrderedDict
import json
d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}

e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}
print(d)
print(e)

# 利用collections模块中的dafaultdict类创建字典（它会自动初始化第一个值）
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)

# 控制字典中元素的顺序
# 使用collections模块中的OrderedDict类
# 当对字典做迭代时，会严格按照元素初始添加的审讯进行：
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:
    print(key, d[key])
# 想在json编码时精确控制各字段的顺序，使用OrderedDict构建数据
print(json.dumps(d))
# OrderedDict内部维护了一个双向链表，来实现字典的有序
# OrderedDict的大小是普通字典的两倍多，使用时应该认真对应用做需求分析，进而减少内存开销。