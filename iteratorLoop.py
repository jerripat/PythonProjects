a_list = [1, 2, 3, 4, 5, 6]

list_iter = iter(a_list)

print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))

for element in a_list:
    print(element)

my_list = [1, 2, 3, 4, 5, 6, 7]

list_iter = iter(my_list)
while True:
    try:
        element = list_iter.__next__()
        print(element)
    except StopIteration:
        break
