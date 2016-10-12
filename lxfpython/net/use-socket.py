#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

#socket.AF_INET IPv4协议， socket.AF_INET6 IPv6协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))

# 发送数据：
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: closer\r\n\r\n')

# 接收数据：
buffer = []
while True:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)

s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
	f.write(html)
