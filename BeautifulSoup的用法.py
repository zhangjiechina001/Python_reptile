import requests
from bs4 import BeautifulSoup
'''
<p class="title">...</p>  p标签 p是标签名称Name， 
BeautifulSoup的五种解析器 html.parser lxml xml html5lib
'''
def get_data(url):
    kv = {'user-agent': 'Mozilla/5.0'}
    try:
        r=requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        # print(r.text[:500])
        return r
    except:
        print('爬取错误')
demo=get_data('http://www.icourse163.org/course/BIT-268001')
soup=BeautifulSoup(demo.text,'html.parser')
print(soup.a)#获得a标签
'''
用 .name获得标签的名字
'''
tag=soup.a
print(tag.attrs)
print(tag.attrs['href'][2:])
print(type(tag))
print(soup.a.string)
print(tag.a.img)