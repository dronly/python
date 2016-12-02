#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def lines(file):
    """
    生成器，在文本最后加一空行
    """
    for line in file:
        yield line
    yield '\n' # 这一行等到上边的for循环结束以后才会执行。

def blocks(file):
    """
    生成器，生成单独的文本块
    当line.strip()为False，block不为空时，才会执行yield 说明，当文本最后一行为空行时，才能返回最后一个文本块
    """
    block = []
    for line in lines(file):
        if line.strip():  # 去掉line的 行首与行尾空格，并判断真假。 字符串为空时 ==》 False
            block.append(line) #如果为真， 将line添加到 block 中
        elif block: #如果line.strip()为假，判断block是否为空。
            yield ''.join(block).strip() #  如果block不为空，将block中的字符串连接其来，连接符为空格
            block = [] # 清除block 缓存。


    
