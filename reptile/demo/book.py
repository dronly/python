#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import time

from bs4 import BeautifulSoup

initial_url = 'https://read.douban.com/columns/category/all?sort=hot&start='
num = 0
start_time = time.time()


def get_detial(url):
    # 获取专栏详细信息  url: 专栏地址
    r = requests.get(url)
    html = r.content
    bsobj = BeautifulSoup(html)

    book_node = bsobj.find('div', class_="info")
    title = book_node.h1.get_text()

    subtitle = book_node.find("div", class_="subtitle").get_text()

    author = book_node.find("a", class_="author-inline labeled-text").get_text()

    category = book_node.find("a", itemprop="url").get_text()

    score = bsobj.findAll("span", class_="score")  # [0].get_text()
    amount = bsobj.findAll("span", class_="amount")  # [0].get_text()
    interactioncount = bsobj.findAll("span", class_="sub-number")
    if len(score) > 0:
        # print(score)
        score = float(score[0].get_text())
    else:
        score = 0
    if len(amount) > 0:
        amount = amount[0].get_text()
        amount = int(''.join(filter(str.isdigit, amount)))
    else:
        amount = 0
    if len(interactioncount) > 0:
        interactioncount = interactioncount[0].get_text()
        interactioncount = int(''.join(filter(str.isdigit, interactioncount)))
    return [title, subtitle, author, category, score, amount, interactioncount]


with open("book2.txt", "w") as f:

    for i in range(1430, 1790, 10):
        r = requests.get(initial_url + str(i))
        # print(url+str(i))
        html = r.content
        bsobj = BeautifulSoup(html)
        book_list_node = bsobj.findAll('div', class_="info")

        for book in book_list_node:
            link = book.h4.a["href"]
            num += 1
            print(("第%d本书"+str(get_detial(link))[1:-1]) % num)
            f.write(str(get_detial(link))[1:-1]+"\n")

end_time = time.time()
times = end_time - start_time

print("运行时间:", times)
