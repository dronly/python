import requests

s = requests.session()
print(type(s))

url1 = 'http://httpbin.org/cookies/set/sessioncookie/123456789'
url2 = 'http://httpbin.org/cookies'
#
# s.get(url1)
# r = s.get(url2)
# print(r.text)


url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
print(r.cookies)   #读取cookies



