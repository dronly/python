#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

class Student(object):

	def get_score(self):
		return self._score

	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value >100:
			raise ValueError('score must between 0~100!')
		self._score = value


s = Student()
s.set_score(60)
print(s.get_score())
#s.set_score(999)
#print(s.get_score())
class Student1(object):
	
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value >100:
			raise ValueError('score must between 0~100!')
		self._score = value

s = Student1()
s.score = 61
print(s.score)
s.score = 999
print(s.score)
