#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
