#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import time

from bs4 import BeautifulSoup

initial_url = 'https://read.douban.com/columns/category/all?sort=hot&start='
num = 0
start_time = time.time()


def getbook(url, i):
    r = requests.get(url + str(i))
    # print(url+str(i))
    html = r.content
    bsobj = BeautifulSoup(html)
    book_list_node = bsobj.findAll('div', class_="info")
    for book in book_list_node:
        title = book.h4.get_text()
        link = book.h4.a["href"]
        if book.h5 is not None:
            sub_title = book.h5.get_text()
        else:
            sub_title = ""
        author = book.findAll("div", class_="author")[0].a.get_text()
        category = [string for string in book.findAll("div", class_="category")[0].stripped_strings][1]
        intro = book.findAll("div", class_="intro")[0].get_text()
        print("标题:"+title, "\n链接:"+link, "\n副标题:" + sub_title,
              "\n作者:"+author, "\n类型:"+category, "\n介绍:"+intro)
        print('======================================')
    return book_list_node

for i in range(0, 1790, 10):
    #print("第%d本书" % num, )
    getbook(initial_url, str(i))

end_time = time.time()
times = end_time - start_time

print("运行时间:", times)
