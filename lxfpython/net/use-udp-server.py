#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

import socket

# 创建udp 类型sokcet 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口：
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')

while True:
	data, addr = s.recvfrom(1024)
	print(addr)
	print('Received from %s:%s.' % addr)
	s.sendto(('Hellow, %s' % data.decode('utf-8')).encode('utf-8'), addr)
	#s.sendto(b'Hello' + data, addr)

