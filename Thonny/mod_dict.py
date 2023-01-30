def outr(a,b):
    def inner(c,d):
        return c + d
    return inner(a,b)
result = outr(5,10)
print(result)