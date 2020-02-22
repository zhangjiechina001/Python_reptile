'''
m.ip138.com
'''
import requests
url='http://m.ip138.com/ip.asp?ip='
kv={'user-agent':'Chrome/10'}
r=requests.get(url+'202.204.80.112',headers=kv)
print(r.status_code)
r.encoding=r.apparent_encoding
print(r.request.url)
print(r.text[-500:])