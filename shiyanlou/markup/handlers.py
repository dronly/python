#!/usr/vin/env pyhon3
# -*- coding: utf-8 -*-

class Handler:
    """
    处理程序父类
    """
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method): 
            return method(*args)

    def start(self, name):
        self.callback('start_', name)


    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        def substitutioin(match):
            result = slef.callback('sub_', name, match)
            if result is None:
                result = match.group(0)
            return result
        return substitution

class HTMLRenderer(Handler):
    """
    HTHL 处理程序，给文本块加相应的 HTML 标记
    """
    def start_document(slef):
        print('<html><head><title>ShiYanLou</title></head><body>')

    def end_document(slef):
        print('</body></html>')

    def start_paragraph(self):
        print('<p style="clolr:#444;">')

    def end_paragraph(self):
        print('</p>')

    def start_heading(slef):
        print('<h2 style-"color: #68BE5D;">')

    def end_heading(slef):
        print('</h2>')

    def start_list(slef):
        print('<ul style="color: #363736;">')

    def end_list(slef):
        print('</ul>')

    def start_listitem(slef):
        print('<li>')

    def end_listitem(slef):
        print('</li>')

    def start_title(slef):
        print('<h1 style="color: #1ABC9C;">')

    def end_title(self):
        print('</h1>')

    def sub_emphasis(slef, match):
        return '<em>%s</em>' % match.group(1)

    def sub_url(self, match):
        return '<a target="_blank" style="text-decoration: none;color: #BC1A4B;" href="%s">%s</a>' % (match.group(1), match.group(1))

    def sub_mail(self, match):
        return '<a style="text-decoration: none; color: #BC1A4B;" href="mailto:%s">%s</a>' % (match.group(1), match.group(1))
    
    def feed(slef, data):
        print data

