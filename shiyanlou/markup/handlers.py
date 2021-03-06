#!/usr/bin/env pyhon3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)

"""
Handler类 处理程序父类，有一个回调函数 callback 可以根据传入的name参数调用相应的方法。
"""

class Handler: # handler-处理程序
    """
    处理程序父类
    """
    def callback(self, prefix, name, *args): # prefix-字首
        method = getattr(self, prefix + name, None) # getattr（x, y) 等价与 x.y  从一个对象中获得名字为y的属性。
        if callable(method):  # callable 返回某个对象是否可以被调用
            return method(*args)

    def start(self, name):
        self.callback('start_', name)


    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                result = match.group(0)
            return result
        return substitution

class HTMLRenderer(Handler):
    """
    HTHL 处理程序，给文本块加相应的 HTML 标记
    """
    def start_document(self): # document-文件
        print('<html><head><title>ShiYanLou</title></head><body>')

    def end_document(self):
        print('</body></html>')

    def start_paragraph(self):# parahraph-段落
        print('<p style="color: #444;">')

    def end_paragraph(self):
        print('</p>')

    def start_heading(self):
        print('<h2 style="color: #68BE5D;">')

    def end_heading(self):
        print('</h2>')

    def start_list(self):
        print('<ul style="color: #363736;">')

    def end_list(self):
        print('</ul>')

    def start_listitem(self):
        print('<li>')

    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1 style="color: #1ABC9C;">')

    def end_title(self):
        print('</h1>')

    def sub_emphasis(self, match):
        return '<em>%s</em>' % match.group(1)

    def sub_url(self, match):
        return '<a target="_blank" style="text-decoration: none;color: #BC1A4B;" href="%s">%s</a>' % (match.group(1), match.group(1))

    def sub_mail(self, match):
        return '<a style="text-decoration: none; color: #BC1A4B;" href="mailto:%s">%s</a>' % (match.group(1), match.group(1))
    
    def feed(self, data):
        print(data)
