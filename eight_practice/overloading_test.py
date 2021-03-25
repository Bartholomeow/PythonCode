from math import nan
from operator_overloading import Person

a = Person()
b = Person('Anya', 20, 'Ж')
c = Person('Petya', 24, 'М')

print(str(a))
print(str(b))
print(a < b)
print(a <= b)
print(a > b)
print(a >= c)
print(a == b)
print(a != c)
print(a + b)
print(a + c)
print(a - b)
