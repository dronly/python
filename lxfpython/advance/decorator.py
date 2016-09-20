#!/bin/python3.5

def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper
'''
def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print ('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
'''

@log#('execute')
def now():
	print('2015-3-25')

#now()
print(now.__name__)
#f = now

#f()

