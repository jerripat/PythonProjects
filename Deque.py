from collections import deque

q = deque(['user', 'password','token'])
print(q)

d = deque('dql')
for i in d:
    print(i.upper())

deque_contents = list(d)
print(deque_contents)

print(d[-1])
print(d[0])

d.append('john')
d.appendleft('fred')
print(d)

rightmost = d.pop()
print(rightmost)

leftmost = d.popleft()
print(leftmost)

d.extend('jkl')
print(d)

d.extendleft('mno')
print(d)
