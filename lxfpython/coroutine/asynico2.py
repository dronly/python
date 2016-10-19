#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world!(%s)' % threading.currentThread())
    yield from asyncio.sleep(2)
    print('Hellow world!(%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
