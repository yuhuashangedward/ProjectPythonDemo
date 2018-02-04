import requests

resp = requests.get('http://www.baidu.com')

resp.encoding = 'UTF-8'
print(resp.content)