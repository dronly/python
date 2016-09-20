#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

class Student(object):
	
	def __init__(self):
		self.name = 'Dronly'
	
	def __getattr__(self, attr):
		if attr == 'score':
			return 99

print(Student().score)

# 动态链接， 可以将status.user.timeline.list ------>  /status/user/timeline/list
class Chain(object):
	def __init__(self, path = ''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return '123'#self._path

	__repr__ = __str__

print(Chain().work)
#print(Chain().status.user.timeline.list)
