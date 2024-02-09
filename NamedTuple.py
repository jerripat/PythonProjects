from collections import namedtuple

Employee = namedtuple('Employee', ['id', 'name', 'age'])
E_1 = Employee('111', 'Peter Parker', '30')
E_2 = Employee('222', 'Clark Kent', '40')

print("Employee name by index is :", end="")
print(E_1[1])

print("Employee name by key is :", end="")
print(E_2.name)

bat_data = ['333', 'Batman', '28']
batman = Employee._make(bat_data)
print(batman)
batman = (batman._replace(id='777', age='34'))
print(batman)
print(batman._fields)

Point = namedtuple('Point', ['x', 'y'])
Color = namedtuple('Color', ['r', 'g', 'b'])
Pixel = namedtuple('Pixel', Point._fields + Color._fields)
p = Pixel(5,8,128,255,0)
print(p)

