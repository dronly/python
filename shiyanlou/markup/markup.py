#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys,re
from handlers import *
from util import *
from rules import *
import logging
logging.basicConfig(level=logging.INFO)

class Parser:
    """
    解析器父类
    """
    def __init__(self, handler):
        self.handler = handler # 处理程序对象
        self.rules = [] # 判断文本种类规则类列表
        self.filters = [] # 判断 url Email 等正则函数列表 re.sub

    def addRule(self, rule):
        """
        添加规则
        """
        self.rules.append(rule) 

    def addFilter(self, pattern, name):
        """
        添加过滤器 
        """
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        """
        解析
        """
        #print(file)  ---> <_io.TextIOWrapper name='<stdin>' mode='r' encoding='UTF-8'>
        self.handler.start('document')
        for block in blocks(file): # 循环文本块
            for filter in self.filters: # 
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end('document')

class BasicTextParser(Parser):
    """
    纯文本解析器
    """
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis') # 重点内容，两个 * 号之间的文本
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url') # 提取url地址正则。
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail') # 提取emali地址正则

"""
运行程序
"""

handler = HTMLRenderer() # 初始化处理程序，
parser = BasicTextParser(handler) # 初始化文本解析器
parser.parse(sys.stdin) # 执行解析方法
