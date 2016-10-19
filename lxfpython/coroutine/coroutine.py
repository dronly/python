# -*- coding: utf-8 -*-
def consumer():
    r = ''
    print('b')
    while True:
        print('c')        
        #print('r---->%s' % r) #启动后执行到这里，遇见yield暂停
        n = yield r
        print('f')
        if not n:
            #print('d')
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    print('a')
    m = c.send(None)
    print('d')
    #print('m == %s' % m)  
    n = 0
    while n < 1:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        print('e')
        r = c.send(n)
        print('g')
        #print('produce r = %s' % r)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
