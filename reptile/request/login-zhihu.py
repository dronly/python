#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import logging
import time
import http.cookiejar as cookielib
from PIL import Image
import os
logging.basicConfig(level=logging.INFO)
agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0'
headers = {
    'User-Agent': agent
}

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")



# 获取验证码
def get_captcha():
    t = str(int(time.time()*1000))
    captcha_url = 'http://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    # 用pillow 的 Image 显示验证码
    # 如果没有安装 pillow 到源代码所在的目录去找到验证码然后手动输入
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input("please input the captcha\n>")
    return captcha


def get_xsrf():
    '''_xsrf 是一个动态变化的参数'''
    index_url = 'http://www.zhihu.com'
    # 获取登录时需要用到的_xsrf
    index_page = session.get(index_url, headers=headers)
    html = index_page.text
    pattern = r'name="_xsrf" value="(.*?)"'
    # 这里的_xsrf 返回的是一个list
    _xsrf = re.findall(pattern, html)
    print(_xsrf)
    return _xsrf[0]

post_url = 'http://www.zhihu.com/login/phone_num'
postdata = {
    '_xsrf': get_xsrf(),
    'password': 'mayanbo19930109',
    'remember_me': 'true',
    'phone_num': '15620950674',
}

try:
    login_page = session.post(post_url, data=postdata, headers=headers)
    login_code = login_page.text
    print(login_page.status_code)
    print(login_code)
except:
    postdata['captcha'] = get_captcha()
    login_page = session.post(post_url, data=postdata, headers=headers)
    login_code = eval(login_page.text)
    print(login_code['msg'])

def isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    url = "https://www.zhihu.com/settings/profile"
    login_code = session.get(url, allow_redirects=False).status_code
    if int(x=login_code) == 200:
        return True
    else:
        return False


if isLogin():
    print('您已经登录')

