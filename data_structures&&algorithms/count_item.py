from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

words_count = Counter(words)

# 出现频率最高的三个单词
top_three = words_count.most_common(3)

# Counter对象就是一个字典
print(words_count['look'])
print(words_count['eyes'])
print((words_count['look']+1))

# 更新计数
morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    words_count[word] += 1

words_count.update(morewords)


a = Counter(words)
b = Counter(morewords)
c = a + b
d = a - b