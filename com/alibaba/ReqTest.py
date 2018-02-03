import requests

url = 'http://www.baidu.com'
resp = requests.post(url)
print(resp.text)

resp.encoding = 'UTF-8'

print('==============')
print(resp.content)