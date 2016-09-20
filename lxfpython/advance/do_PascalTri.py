#!/bin/python3.5
# -*- coding: utf-8 -*-
def triangles():
	L=[1]	
	while True:
		yield L
		L1=[0] + L[:]
		L = [ L[i] + L1[i] for i in range(len(L))] + [1]
		

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
A=[1, 2, 3, 4]
A1 = [0] + A[:]
print (A1)

def Iterator():
    i=1
    while True:
        yield i
        i+=1
o=Iterator
for t in o():
    print(t)
