#!/usr/bin/env python3
# -*- codong: utf-8 -*- 

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
a = cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
print(a)

cursor.execute('insert into user(id, name) values (\'1\', \'Dronly\')')
cursor.rowcount

# 关闭cursor
cursor.close()
# 提交事务
conn.commit()
# 关闭Connection
conn.close()

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#执行查询语句：
cursor.execute('select * from user where id=?', ('1',))
value = cursor.fetchall()
print(value)

# 关闭cursor
cursor.close()
# 提交事务
conn.commit()
# 关闭Connection
conn.close()
