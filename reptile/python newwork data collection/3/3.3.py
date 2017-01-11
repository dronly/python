#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())


def getInternalLinks(bsobj, includeUrl):
    '''
    获取页面所有內链列表
    :param bsobj:
    :param includeUrl:
    :return:
    '''
    internalLinks = []
    # 找出所有以"/"开头的链接
    for link in bsobj.findAll('a', href=re.compile('^(/|.*'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks


def getExternalLinks(bsobj, excludeUrl):
    '''
    获取页面所有的外链列表
    :param bsobj:
    :param excludeUrl:
    :return:
    '''
    externalLinks = []
    # 找出所有以'http' 'www' 开头且不包含当前URL的链接
    for link in bsobj.findAll('a',
                              href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace('http://', '').split('/')
    return addressParts


def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsobj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsobj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getExternalLinks(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink("http://oreilly.com")
    print("随机外链是:" + externalLink)
    followExternalOnly(externalLink)


followExternalOnly("http://oreilly.com")