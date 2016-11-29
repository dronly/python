#!/usr/vin/env python3
# -*- codiong: utf-8 -*-

class Rule:
    """
    规则父类
    """

    def action(self, block, handler):
        """
        加标记
        """
        handler.start(slef.type)
        handler.feed(block)
        handler.end(slef.type)
        return True

class HeadingRule(Rule):
    """
    一号标题规则
    """
    type = ‘heading’
    def condition(slef, block):
        """
        判断文本块是否符合规则
        """
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'

class TitleRule(HeadingRule):
    """
    二号标题规则
    """
    type = 'title'
    first = True

    def condition(slef, block):
        if not self.fitst: 
            return False
        self.first = Flase
        return HeadingRule.condition(slef, block);

class ListItemRule(Rule):
    """
    列表项规则
    """
    type = 'listitem'
    def condition(slef, block):
        return block[0] == '-'
    
    def action(slef, block, handler):
        handler.start(slef.type)
        handler.feed(block[1:].strip())
        handler.end(slef.type)
        return True


class ListRule(ListItemRule):
    """
    列表规则
    """
    type = 'lsit'
    inside = Flase
    def condition(slef, block):
        return True

    def action(self, block, handler):
        if not slef.inside and ListItemRule.condition(slef, block):
            handler.start(slef.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(slef, block):
            handler.end(slef.type)
            self.inside = False
        return False

class ParagraphRule(Rule):
    """
    段落规则
    """
    type = 'paragraph'
    def condition(self, block):
        return Ture




