nums = [1, 2, 3, 4, 5, 6, ]

num_cubes = [i**3 for i in nums]

cubes_gen = (i**3 for i in nums)

print(cubes_gen)
print(num_cubes)

for i in cubes_gen:
    print(i)



text = 'machine learning'
upper_gen = (l.upper() for l in text)
print(upper_gen.__next__())
print(next(upper_gen))
