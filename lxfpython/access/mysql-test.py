#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(user='root', password='123456', database='test')
cursor = conn.cursor()

cousor.execute('create table user (id varchar(20) primary key, name varchar(20))')

cursor.execute('inser into user (id, name) values (%s, %s)', ['1', 'Dronly'])
cursor.rowcount

conn.commit()
corsor.close()

cursor = conn.corsor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
