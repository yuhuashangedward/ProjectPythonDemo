import requests

r = requests.get('http://www.baidu.com');

print(r.encoding)
print(r.status_code)
print(r.text)
print(r.content)
print(r.url)