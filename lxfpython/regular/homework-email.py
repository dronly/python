#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re

#email = 'bill.ga@tes@microsoft.com'
#a = re.match(r'(.+?)@\w+.com', email)
#print(a.group(1))


s1 = 'someone@gmail.com'
s2 = 'bill.gares@microsoft.com'
s0 = 'jimmy.Wang@zzu.edu.cn'

pattern1 = r'^[\w\_\.]+@[0-9a-z]+\.[a-z]+$'
pattern2 = r'^(\w+[\w.]*?\w+)@{1}(\w+[\w.]+?\w+)$'
re_email = re.compile(pattern2)
print(re_email.match(s1).group())
print(re_email.match(s2).group())
print(re_email.match(s0).group())

s3 = "<Tom Paris> tom@voyager.org"
pattern = r'^<([a-zA-Z]+\s+[a-zA-Z]+)>\s+([0-9a-zA-Z\_\.]+@[0-9a-z]+\.[a-z]+)$'
re_nameemail = re.compile(pattern)
print(re_nameemail.match(s3).group(1))
