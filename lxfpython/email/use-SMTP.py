#!/usr/bin/env python3
# -*- coding:  utf-8 -*- 

# 网易服务器地址  POP3服务器: pop.163.com	SMTP服务器: smtp.163.com		IMAP服务器: imap.163.com

from email.mime.text import MIMEText
from email.header import Header
import smtplib 
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['Subject'] = Header('放假通缉', 'utf-8')
msg['From'] = 'xxxxx@163.com>'
msg['To'] = "&&&&&&@ttop9.com"

# 输入Email地址和口令：
from_addr = input('From: ')
password = input('Password: ')

# 输入收件人地址：
to_addr = input('To:')
# 输入SMTP服务器地址：
smtp_server = input('SMTP server:')


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
