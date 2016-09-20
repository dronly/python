#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

#定制类 __iter__

#斐波那契数列
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1


	def __iter__(self):
		return self   # 

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b #计算下一个值
		if self.a > 100000:
			raise StopIteration();
		return self.a
#print(Fib().b)
for n in Fib():
	print(n)
