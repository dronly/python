#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import argparse
from PIL import Image

parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o')
parser.add_argument('-output')
parser.add_argument('--width', type = int, default = 80)
parser.add_argument('--height', type = int, default = 80)

args = parser.parse_args()

IMG = args.file
OUTPUT = args.output
HEIGHT = args.height
WIDTH = args.width

ascii_str = list("1234567890!@#$%^&*()qwertyuioplkjhgfdsazxcvbnm,./';[]<>?:")

def get_char(r, g, b, alpha = 256):
	if alpha == 0:
         return ' '
	gray = int(0.2126*r + 0.7152*g + 0.0722*b )
	lengs = len(ascii_str)
	unit = (1+256.0) / lengs
	return ascii_str[int(gray/unit)]

#print(get_str(221,1,12))

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print (txt)

    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)





