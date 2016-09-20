#!/bin/python3.5
from collections import Iterable

d = {'a':1, 'b':2, 'c':3}
for key in d:
	print(key)

for value in d.values():
	print(value)

for ch in 'ABC':
	print(ch)

print(isinstance('abc', Iterable) )
print(isinstance(123,Iterable))

for i, value in enumerate(['a', 'b', 'c']):
	print(i, value)

for x,y in [(1,1), (2,4), (3,9)]:
	print(x,y)

list(range(1, 11))
print(list)
