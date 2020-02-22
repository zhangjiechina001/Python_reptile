import requests

kv={'user-agent':'Mozilla/5.0'}
url='https://www.amazon.cn'
r=requests.get(url,headers=kv)
r.encoding=r.apparent_encoding
print(r.status_code,r.request.headers)
def get_data(url):
    kv = {'user-agent': 'Mozilla/5.0'}
    try:
        r=requests.get(url,headers=kv)
        r.raise_for_status()
        print(r.text[:500])
    except:
        print('爬取错误')

if __name__=='__main__':
    get_data(url)