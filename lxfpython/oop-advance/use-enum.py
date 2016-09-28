#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nob', 'Dec'))

for name, member in Month.__members__.items():
	print(name,'==>', member,',',  member.value)

print(Month.Jan.name)


# unique 装饰器可以检查保证没有重复值
@unique
class Weekday(Enum):
	sun = 0 # Sun的value被设定为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])

for name,  member in Weekday.__members__.items():
	print(name, '-->', member)
print(Weekday.Tue.value)
