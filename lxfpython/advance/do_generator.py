#!/bin/python3.5
# -*-coding: utf-8 -*-
#Filename do_generator.py

#create 2016.9.1 Dronly Ma
L = [x*x for x in range(10)]
print (L)

g = (x*x for x in range(10))
print (g)

for n in g:
	print (n)

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield(b)
		a,b = b, a+b
		n = n+1
	return 'done'

for x in fib(6):
	print(x)

g = fib(6)
while True:
	try:
		x = next(g)
		print('g', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break
