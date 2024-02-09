class Odd:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            current_value = self.current
            self.current += 2
            return current_value
        else:
            raise StopIteration


odd_numbers = Odd(20)
print(odd_numbers.__next__())
print(odd_numbers.__next__())
print(next(odd_numbers))
print(next(odd_numbers))

if __name__ == "__main__":
    print(__file__)