#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module'

__author__ = 'Dronly My'

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print('Hellow world')
	elif len(args)==2:
		print('Hellow , %s' % args[1])
	else:
		print('Too many arguements!')

if __name__ == '__main__':
#if __name__=='__main__':
	test()

def _private_1(name):
	return 'Helow, %s' % name

def _private_2(name):
	return 'Hi ,%s' % name

def greeting(name):
	if len(name)>3 :
		return _private_1(name)
	else :
		return _private_2(name)
