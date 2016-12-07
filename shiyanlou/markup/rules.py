#!/usr/vin/env python3
# -*- codiong: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)

"""
这个模块内容是给每一种文本类型（一级标题，二级标题，列表等）定义判断规则。
每一个Rule子类都有condition方法，用来判断文本是否它符合规则。从Rule继承的action方法用来给符合的文本加标记。
"""

class Rule:
    """
    规则父类
    """

    def action(self, block, handler):
        """
        加标记
        """
        handler.start(self.type) # 标签头
        handler.feed(block) # 标签内容
        handler.end(self.type) # 标签尾
        return True

class HeadingRule(Rule):
    """
    一号标题规则
    判断文本块是否是标题
    """
    type = 'heading'
    def condition(self, block):
        """
        判断文本块是否符合规则
        """
        # 当不含有换行符，长度大于70 不以：结尾时， block为 标题。
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'


"""
TitleRule与HeadingRule 结合起来判断标题是一级标题还是二级标题。
在 markup.py 中的 BasicTextParser 中先添加 TitleRule 规则，后添加 HeadingRule 规则。
根据 TitleRule 规则可以知道，会把第一个 block 设为一级标题，后边的 block 都会调用 HeadingRule 规则。
"""
class TitleRule(HeadingRule):
    """
    二号标题规则
    判断是否是第一次出现标题。
    action 方法打印 <h1 style="color: #1ABC9C;">%s</h1>
    """
    type = 'title'
    first = True

    def condition(self, block):
        if not self.first: 
            return False
        self.first = False
        return HeadingRule.condition(self, block);

class ListItemRule(Rule):
    """
    列表项规则
    """
    type = 'listitem'
    def condition(self, block):
        return block[0] == '-'
    
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True


class ListRule(ListItemRule):
    """
    列表规则
    """
    type = 'list'
    inside = False
    def condition(self, block):
        return True

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False

class ParagraphRule(Rule):
    """
    段落规则
    """
    type = 'paragraph'
    def condition(self, block):
        return True




