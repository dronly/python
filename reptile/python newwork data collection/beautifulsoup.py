#!/usr/bin env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError


'''
html = request.urlopen(url)
bsObj = BeautifulSoup(html.read())
print(bsObj.div)
'''


url = 'http://www.pythonscraping.com/pages/page1.html'
url2 = 'http://www.pythonscraping.com/pages/warandpeace.html'


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:  # 服务器没有这个页面
        return None
    except URLError as e:  # 服务器不存在
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title





html = urlopen(url2)
bsObj = BeautifulSoup(html)
nameList = bsObj.findAll('span', {'class': 'green'})

# for name in nameList:
#     print(name.get_text())

# pricelist = bsObj.findAll(text='the prince')
# print('the prince:=', pricelist)

# if title == None:
#     print('Title could not be found')
# else:
#     print(title)


def keyworld():
    allText = bsObj.findAll(id='text')
    print(allText[0].get_text())


# keyworld()
taburl = 'http://www.pythonscraping.com/pages/page3.html'


def tabtest():
    html = urlopen(taburl)
    bsObj = BeautifulSoup(html)

    for child in bsObj.find('table', {'id': 'giftList'}).children:
        print(child)

tabtest()
