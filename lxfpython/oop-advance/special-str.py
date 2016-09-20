#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

class Student(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'Student object (name: %s)' % self.name

print(Student('Dronly'))
'''<__main__.Student object at 0x7f0b45a7df98>
user@user-Z97-HD3 /work/Study/python/lxfpython/oop-advance $ python3.5 special-str.py 
Student object (name: Dronly)'''

