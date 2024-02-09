from time import time

def first_n_numbers(max):
    n, numbers = 0, []
    while n <= max:
        numbers.append(n)
        n += 1
    return numbers

start = time()
first_n_list = first_n_numbers(10000000)
sum_of_first_numbers = sum(first_n_list)

print(sum_of_first_numbers)


end = time()
print("Elapsed Time in seconds: ", end - start)

def first_n_numbers_generator(max):
    n = 1
    while n <= max:
        yield n
        n += 1

start = time()
first_n_generator = first_n_numbers_generator(10000000)
sum_of_first_numbers = sum(first_n_generator)

print(sum_of_first_numbers)


end = time()
print("Elapsed Time in seconds: ", end - start)
