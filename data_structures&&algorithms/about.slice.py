record = '.......100 .....53........'
cost = int(record[7:10]) * int(record[16:18])
amount = slice(7, 10)
price = slice(16, 18)
cost_new = int(record[amount]) * int(record[price])

# 开始 结束 步长
a = slice(5, 50, 2)
print(a.start)
print(a.stop)
print(a.step)

s = 'HelloWorldmadzz'
print(a.indices(len(s)))
print(a.start)
print(a.stop)
print(a.step)

for i in range(*a.indices(len(s))):
    print(s[i])