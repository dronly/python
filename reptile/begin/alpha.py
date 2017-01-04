import re
import urllib
import urllib.request
import logging
from collections import deque

logging.basicConfig(level=logging.DEBUG)


queue = deque()
visited = set()

# url = 'http://news.dbanotes.net/'
url = 'http://www.baidu.com'
queue.append(url)
cnt = 0

while queue:
    logging.debug(queue)
    url = queue.popleft()
    visited |= {url}

    print('已经抓取了： ' + str(cnt) + '  正在抓取<---- ' + url)
    cnt += 1

    try:
        urlop = urllib.request.urlopen(url)
        # logging.debug('urlop')
    except:
        logging.debug('urlop: 第' + str(cnt) + "次抓取失败")
        continue

    if 'html' not in urlop.getheader('Content-Type'):
        logging.debug('返回的数据不包含 html')
        continue

    try:
        data = urlop.read().decode('utf-8')
        logging.debug('抓取返回的数据：')
    except:
        logging.debug('解析数据失败')
        continue

    linkre = re.compile(r'href="(.+?)"')
    logging.debug(linkre.findall(data))
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列 --->  ' + x)
