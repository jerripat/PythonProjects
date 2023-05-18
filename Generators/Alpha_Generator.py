import string


def letters():
    yield from string.ascii_lowercase


for letter in letters():
    print(letter)
