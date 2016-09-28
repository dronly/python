#!/usr/bin/env python3.5
#-*- coding: utf-8-*-

def fn(self, name = 'world'): # 定义函数
	print('Hellow, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) #创建Hello class
h = Hello()
h.hello()

print(type(Hello))

print(type(h))
