from collections import defaultdict

s = [('yellow',1), ('green',2), ('red',3), ('blue',4), ('purple',5)]
d = defaultdict(list)
for k,v in s:
    d[k].append(v)

sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(sorted_items)