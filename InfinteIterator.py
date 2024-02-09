class infiniteCounter:
    def __init__(self):
        self.n = 1

    def __iter__(self):
        return self

    def __next__(self):
        current = self.n

        return current

    counter = infiniteCounter()
    print