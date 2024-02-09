tup = ('a', 'b', 'c')
tup_iter = iter(tup)
item_1 = next(tup_iter)
print(item_1)
item_2 = next(tup_iter)
print(item_2)
item_3 = next(tup_iter)
print(item_3)

pyt = 'python'
pyt_itr = pyt.__iter__()

item_1 = pyt_itr.__next__()
print(item_1)

item_2 = pyt_itr.__next__()
print(item_2)

item_3 = pyt_itr.__next__()
print(item_3)
