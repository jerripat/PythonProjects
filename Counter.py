from collections import Counter

c1 = Counter()
print(c1)

c2 = Counter('aabbbcddeeee')
print(c2)

c3 = Counter({'orange': 1, 'apple': 2, 'banana': 3})
print(c3)

c4 = Counter(cats=4,dogs=8)
print(c4)

c5 = Counter(['eggs','ham','jar'])
print(c5['ham'])
c5['sausage'] = 0
print(c5)

del c5['sausage']
print(c5)




