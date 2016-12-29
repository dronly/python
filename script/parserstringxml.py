#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.dom.minidom
import re
import argparse
import sys
import os

# 功能： 将 strings.xml 中含有格式化字符串，时间格式化字符串的条目提取出来并保存
# 2016-12-19

"""
解析xml文件返回 list
"""


def parserStringXml(file):
    dom = xml.dom.minidom.parse(file)
    root = dom._get_documentElement()
    stringslist = root.getElementsByTagName('string')
    listtmp = []
    # return [string.getAttribute('name') if  for string in stringslist]
    for string in stringslist:
        name = string.getAttribute('name')

        if(hasattr(string.firstChild, "data")):
            data = string.firstChild.data
            # print("sss" + string.getAttribute('formatted'))
            #if judegFormatString(data):
            if string.getAttribute('formatted')=='':
                listtmp.append([name, data])
            else:
                # print('aaa')
                continue
            #print(name, '=', data)
        # else:
        #     listtmp.append(name)
    return listtmp


def writeStringXml(list, file):
    with open(file, "w") as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n')
        f.write('<resources>\n')
        for string in list:
            f.write('    <string name="'+string[0]+'">'+string[1]+'</string>\n')
        f.write('</resources>')

def judegFormatString(string):
    timeFormatString = ["%1$dd %2$dh %3$dm %4$ds","%1$dh %2$dm %3$ds", "%1$dm %2$ds", "%1$dd %2$dh %3$dm",
    "%1$dh %2$dm", "%1$d day %2$d hrs", "%1$d day %2$d hr", "%1$d hrs",
    "%1$d hr %2$d mins", "%1$d hr %2$d min", "%1$d mins", "%1$d min",
    "%1$d min %2$d secs", "%1$d min %2$d sec", "%1$d secs", "%1$d sec",
    "%1$02d:%2$02d", "%1$d:%2$02d:%3$02d", "%Y-%m-%d",
    "%Y-%m-%dT%H:%M:%S", "%s%s%02d:%02d", "%d-%02d-%02d"]
    for tfs in timeFormatString:
        if tfs in string:
            return True

    filter = r'.*%[0-9]{1}\$[sd]{1}|%[sd]{1}'
    formatString = re.match(filter, string)
    if formatString != None:
        return True
    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='统计apk的strings.xml中格式化字符串数量脚本')
    parser.add_argument('filePaths', nargs='+', help='输入反编译apk后得到的strings.xml路径')
    parser.add_argument('-o', '--output', help='输出目录，输出提取出来的格式化字符串到输出目录下的format_string.xml')
    args = parser.parse_args()

    if args.filePaths[-3:] == 'xml':
        print('请输入xml文件路径')
        sys.exit()

    if args.output is not None:
        if not os.path.isdir(args.output):
            print('Invalid Directory: ' + args.output)
            sys.exit()
        else:
            if args.output[-1] != '/':
                args.output += '/'
        args.output += 'format_strings.xml'
    else:
        args.output = 'format_strings.xml'
    listString = parserStringXml(args.filePaths[0])
    tmplist = []
    for list in listString:
        if judegFormatString(list[1]):
            tmplist.append(list)
    writeStringXml(tmplist, args.output)
    print('strings 总数量：', len(listString))
    print('含有格式化字符串的 strings 数量：', len(tmplist))
    print('格式化字符串占的百分比：', format(len(tmplist)/len(listString), '.2%'))
