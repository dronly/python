#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta
from datetime import timezone

now = datetime.now() #获取当前datetime
print(now)

dt = datetime(2015, 4, 19, 12, 20)  #用指定日期时间创建datetime
print(dt)

# 1970年1月1日 00：00：00 UCT+00：00 时区的时刻为0

timestamp = dt.timestamp() # 把datetime转换为timestamp
print(timestamp)



# timestamp 转换为datetime 
t = 1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))	# UTC时间

# 字符串转换成datetime

cday = datetime.strptime('2016-10-9 10:50:50', '%Y-%m-%d %H:%M:%S')
print(cday)

# 日期加减
now = datetime.now()
print(now)
a = now+timedelta(hours=10)
print(a)
b = now+timedelta(days=1)
print(b)


#时区转换
#拿到UTC时间， 并强制设置时区为UTC+0：00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
#astimezone() 将转换为时区为北京时间：
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

