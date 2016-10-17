def consumer():
    r = ''
    #print('a')
    while True:
        #print('r---->%s' % r) #启动后执行到这里，遇见yield暂停
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    m = c.send(None)
    #print('m == %s' % m)  
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        #print('produce r = %s' % r)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
