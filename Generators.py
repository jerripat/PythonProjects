def first_generator():
    print("first generator")
    yield 'A'

    print("second generator")
    yield 'B'

    print("third generator")
    yield 'C'

iter_obj = first_generator()
first_item = next(iter_obj)
print(first_item)

second_item = next(iter_obj)
print(second_item)

third_item = next(iter_obj)
print(third_item)


first_generator()
