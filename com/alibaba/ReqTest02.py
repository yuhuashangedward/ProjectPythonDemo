import requests

r = requests.get('http://www.zhidaow.com')

# 返回码
print(r.status_code)

#返回头部信息
print(r.headers['content-type'])

print(r.encoding)

print(r.text)