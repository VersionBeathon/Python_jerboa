# prices字典在股票名和对应的价格上做了映射

price = {
    'ACMS': 23.123123,
    'ARCHER': 45894859.11,
    'IBM': 123123.111,
    'APPLE': 998,
    'ZAPER': 13
}
# 为了能对这样的字典进行计算，利用zip()将字典的键值反转
# 求最小最大价格
min_price = min(zip(price.values(), price.keys()))
print(min_price)
max_price = max(zip(price.values(), price.keys()))
print(max_price)
# 按照价格对股票进行排序
price_sorted = sorted(zip(price.values(), price.keys()))
print(price_sorted)

# zip()创建了一个迭代器，生成内容只能被消费一次。
price_names = zip(price.values(), price.keys())
print(max(price_names))
'''print(min(price_names)) 由于zip()产生的结果只能被消费一次所以此处错误'''

# 在字典上的数据操作，只会处理键
print(min(price))
print(max(price))
# 如果想处理字典的值
print(min(price.values()))
print(max(price.values()))