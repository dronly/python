#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

def fact(n):
	'''
	>>> fact(-1)
	Traceback (most recent call last):
		...
	ValueError
	>>> fact(1)
	1
	>>> fact(2)
	2
	>>> fact(9)
	362880
	'''
	if n < 1:
		raise ValueError()
	if n == 1:
		return 1 
	return n*fact(n-1)

if __name__ == '__main__':
	import doctest
	doctest.testmod()
