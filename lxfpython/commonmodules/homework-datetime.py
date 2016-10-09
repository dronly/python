#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
	dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')#提取出当前时间
	tz = re.match(r'^UTC([+|-]\d+):00$', tz_str).group(1)
	nowtimezone = timezone(timedelta(hours=int(tz)))#提取时区
	nowdatetime = dt.replace(tzinfo=nowtimezone)
	return nowdatetime.timestamp()



t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print (t1, t2)

print('Pass')
