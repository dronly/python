#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import parserstringxml
import argparse
import sys
import os

# 功能 把translate下所以的app的string.xml 中含有格式化字符串以及时间格式化字符串的条目
# 提取出来 并保存到目标路径， 输入每个app中格式化字符串占的百分比以及总共的百分比到
#percent.txt 中。
# 2016-12-19

def makedir(path):
    dirname = os.path.split(path)[0]
    if not os.path.exists(dirname):
        print('成功创建'+dirname)
        os.makedirs(dirname)

parser = argparse.ArgumentParser(description='多国语言项目格式化字符串统计')
parser.add_argument('input',  help='输入目录：给出需要分析的项目下 translate 路径')
parser.add_argument('output',  help='输出目录： 给出分析结果保存的路径')
args = parser.parse_args()
sourcePath = args.input
outputPath = args.output
if not os.path.exists(outputPath):
    os.makedirs(outputPath)


persentmap = {}
formatstring = 0
allstring = 0

appdirlist = ['app', 'framework', 'priv-app']
for appdirs in appdirlist:
    targetappdirs = os.path.join(outputPath, appdirs)
    appdirs = os.path.join(sourcePath, appdirs)
    for appname in os.listdir(appdirs):
        targetfile = os.path.join(targetappdirs, appname, 'translated_online_res/values-af/strings.xml')
        print(targetfile)
        makedir(targetfile)
        inputfile = os.path.join(appdirs, appname, 'res/values/strings.xml')
        print(inputfile)
        if not os.path.exists(inputfile):
            continue
        listString = parserstringxml.parserStringXml(inputfile)
        tmplist = []
        for list in listString:
            if parserstringxml.judegFormatString(list[1]):
                tmplist.append(list)
        parserstringxml.writeStringXml(tmplist, targetfile)
        persentmap[appname] = format(len(tmplist)/len(listString), '.2%')
        formatstring += len(tmplist)
        allstring += len(listString)
if outputPath[-1] != '/':
    outputPath += '/'
outputfile = outputPath + 'percent.txt'
with open(outputfile, 'w') as f:
    for k, v in persentmap.items():
        f.write(k+'='+v+'\n')
    f.write('All format string number =' + str(formatstring)+'\n')
    f.write('All string numner =' + str(allstring)+'\n')
    f.write('All app format persent =' + format(formatstring/allstring, '.2%'))
