#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

class Student(object):
	__slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
class GraduateStudent(Student):
	pass

s = Student() 	#创建新的实例
s.name = 'Dronly'
s.age = 24

try:
	s.score = 99
except AttributeError as e:
	print('AttributeError:', e)

g = GraduateStudent()
g.score = 99
print('g.score = ',g.score)
