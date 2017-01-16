#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

url = 'http://e.weather.com.cn/d/air/101010100.shtml'
r = requests.get(url)
print(r.text)
