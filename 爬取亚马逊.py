import requests

kv={'user-agent':'Mozilla/5.0'}
url='https://www.baidu.com'
r=requests.get(url,headers=kv)
r.encoding=r.apparent_encoding
print(r.status_code,r.request.headers)
def get_data(url):
    kv = {'user-agent': 'Mozilla/5.0'}
    try:
        r=requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print(r.text[:500])
        return r
    except:
        print('爬取错误')

if __name__=='__main__':
    # data=get_data(url)
    r=requests.get('http://python123.io/ws/demo.html')
    print(r.text)