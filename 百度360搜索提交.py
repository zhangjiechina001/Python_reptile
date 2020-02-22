import requests
'''
百度关键词接口：http://www.baidu.com/s?wd=keyword
360关键词接口: http://www.so.com/s?q=keyword
'''
def get_data(url,kv,resercher_fun=None):
    try:
        header={'user-agent':'Chrome/10 '}
        r=requests.get(url,params=kv,headers=header)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print(r.request.url)
        print(r.text[:1000])
    except:
        print('爬取错误！')

if __name__=='__main__':
    url='http://www.baidu.com/s'
    kv={'wd':'合肥工业大学'}
    get_data(url,kv)