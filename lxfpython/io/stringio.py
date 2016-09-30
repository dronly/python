#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-
from io import StringIO
f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world!'))

print(f.getvalue())
f = StringIO('Hellow!\nHi\nGoodbye!')

while True:
	s = f.readline()
	if s == "":
		break
	print(s.strip())

