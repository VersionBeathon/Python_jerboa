# _*_ coding:utf-8 _*_
# 将键（key）映射到多个值的字典（一键多值字典[multidict]）
from collections import defaultdict
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
