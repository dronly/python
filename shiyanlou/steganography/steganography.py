#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image


def makeimageeven(image):
    pixels = list(image.getdata())  # 获得 image 的像素信息列表
    # 通过位运算，将 pixels 每个元素的最后一位设为0
    evenpixels = [(r >> 1 << 1, g >> 1 << 1, b >> 1 << 1, t >> 1 << 1) for [r, g, b, t] in pixels]
    evenimage = Image.new(image.mode, image.size)  # 创建一个与 image 相同大小相同格式的图片
    evenimage.putdata(evenpixels)  # 给 evenimage 添加像素信息。
    return evenimage

  
def constlenbin(intnumber):  # 这个函数就是将以'ob'开头的不等长二进制数转化为8位二进制数
    binary = "0" * (8-(len(bin(intnumber))-2)) + bin(intnumber).replace('0b', '')  # bin 函数 讲整形数字转换成二进制形式，
    return binary

    
def encodedatainimage(image, data):  # 把数据存入到image中。
    evenimage = makeimageeven(image)  # 把参数 image 每个像素点的最后以为改成0
    binary = ''.join(map(constlenbin, bytearray(data, 'utf-8')))  # map 高阶函数，第一个参数传入函数 constlenbin 第二个参数传入 list
    if len(binary) > len(image.getdata()) * 4:  # 如果 binary 长度大于 image.getdata()*4 说明需要存入的数据太大， image 不能写下
        raise Exception("Error: Can't encode more than" + len(evenimage.getdata()) * 4 + " bits in this image. ")
    # 这一长句的作用就是把 binary 中的每一位依次放入到 evenimage.getdata() 中的 rgbt 值的最后一位。用到了列表生成器， enumerate 函数--》同时列表索引以及值。
    encodedpixels = [(r+int(binary[index*4+0]), g+int(binary[index*4+1]), b+int(binary[index*4+2]),
                      t+int(binary[index*4+3]))if index*4 < len(binary)
                     else (r, g, b, t) for index, (r, g, b, t) in enumerate(list(evenimage.getdata()))]
    encodedimage = Image.new(evenimage.mode, evenimage.size) 
    encodedimage.putdata(encodedpixels)
    return encodedimage


def binarytostring(binary):  # 将二进制数据转化位 str
    index = 0
    string = []
    rec = lambda x, i: x[2:8] + (rec(x[8:], i-1) if i > 1 else '') if x else ''
    fun = lambda x, i: x[i+1:8] + rec(x[8:], i-1)
    while index + 1 < len(binary):
        chartype = binary[index:].index('0')
        length = chartype*8 if chartype else 8
        string.append(chr(int(fun(binary[index:index+length], chartype), 2)))
        index += length
    return ''.join(string)

    
def decodeimage(image):  # 把 image 图片中隐藏的数据拿出来。
    pixels = list(image.getdata())
    binary = ''.join([str(int(r >> 1 << 1 != r))+str(int(g >> 1 << 1 != g))+str(int(b >> 1 << 1 != b)) +
                      str(int(t >> 1 << 1 != t)) for (r, g, b, t) in pixels])
    locationdoublenull = binary.find('0000000000000000')
    endindex = locationdoublenull + (8-(locationdoublenull % 8)) if locationdoublenull % 8 != 0 else locationdoublenull
    data = binarytostring(binary[0:endindex])
    return data

encodedatainimage(Image.open("coffee.png"), '你好世界，Hello world!').save('encodeImage.png')
print(decodeimage(Image.open("encodeImage.png")))
