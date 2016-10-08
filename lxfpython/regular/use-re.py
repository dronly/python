#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# re模块，包含所有的正则表达式的功能。 

import re
a = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(a)

b = re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
print(b)
