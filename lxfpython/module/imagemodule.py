#!/usr/bin/env python3.5
from PIL import Image

im = Image.open('Screenshot.png')
print(im.format, im.size, im.mode)

im.thumbnail((200,100))
im.save('thumb.jpg','JPEG')
