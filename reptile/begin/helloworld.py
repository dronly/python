# coding: utf-8 -*-

import urllib.request

# url = 'http://www.baidu.com'
#
# data = urllib.request.urlopen(url).read()
# data = data.decode('UTF-8')
# # print(data)
#
# # a = urllib.request.urlopen(url)
# # prinht(type(a))
# #
# # print(a.geturl())
# # print(a.info())
# # print(a.getcode())


data = {}

data['word'] = 'Jecvay Notes'

url_values = urllib.parse.urlencode(data)
url = 'http://www.baidu.com/s?'

full_url = url+url_values

data = urllib.request.urlopen(full_url).read()
data = data.decode('UTF-8')
print(data)
