#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def run(self):
		print('Dog is running...')
	def eat(self):
		print('Eating meat...')

class Cat(Animal):
	def run(self):
		print('Cat is running...')

class Tortolse(Animal):
	def run(self):
		print('Tortoise is running slowly...')

class Timer(object):
	def run(self):
		print('Start...')

dog=Dog()
dog.run()
cat = Cat()
cat.run()
def run_twice(a):
	a.run()
	a.run()

run_twice(dog)
run_twice(Timer())
