#!/usr/bin/env python3
import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

json_str = '{"age": 20, "name": "Bob", "score": 88}'
print(json.loads(json_str))

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

def student2dict(std):
	return {
		'name': std.name,
		'age': std.age,
		'score': std.score
	}

s = Student('Bob', 20, 88)

print(json.dumps(s, default=lambda obj: obj.__dict__))
