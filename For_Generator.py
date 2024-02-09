def get_sequence_gen(max):
    for n in range(max):
        yield n
sequence_iter = get_sequence_gen(10)
print(sequence_iter.__next__())
print(sequence_iter.__next__())
print(next(sequence_iter))
print(next(sequence_iter))
