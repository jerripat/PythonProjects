from collections import ChainMap

numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
letters = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E'}

chain_map = ChainMap(numbers, letters)

print(chain_map)

print(chain_map.keys())
print(chain_map.values())

print(chain_map['one'])

variables = {'x': 1, 'y': 2, 'z': 3}
new_chain_map = chain_map.new_child(variables)

print('Old', chain_map)
print('New', new_chain_map)

print(chain_map.maps)
