'''
第一页//search.jd.com/Search?keyword=书包&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=书包&stock=1&page=3&s=61&click=0
第二页//search.jd.com/Search?keyword=书包&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=书包&stock=1&page=3&s=61&click=0
第三页//search.jd.com/Search?keyword=书包&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=书包&stock=1&page=5&s=121&click=0
第三页//search.jd.com/Search?keyword=书包&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=书包&stock=1&page=9&s=241&click=0
https://search.jd.com/Search?keyword=%E4%B9%A6%E5%8C%85&enc=utf-8&wq=%E4%B9%A6%E5%8C%85&pvid=d74adeb5749345c1ae182aa6900ac2dd
https://search.jd.com/Search?keyword=%E4%B9%A6%E5%8C%85&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E4%B9%A6%E5%8C%85&stock=1&page=3&s=61&click=0
'''
# 最好大学排名信息爬取
import bs4
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# coding=utf-8
def getHtmlText(url):
    kv = {'user-agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=kv, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('爬取错误')

def fillUnivList(html):
    soup = BeautifulSoup(html, 'html.parser')
    soup.prettify()
    #     print()
    print(soup)
    trs=soup.find('ul','gl-warp clearfix').find_all('li','gl-item')
    ulist=[]
    for tr in trs:
        #将不是标签的数据过滤掉，最后一个黄山学院就不是标签数据
        if isinstance(tr,bs4.element.Tag):
            div_value=tr.find('div','gl-i-wrap')
            div_value.prettify()
            div_price=div_value.find('div','p-price').find('strong').find('i').string
            # 产品介绍
            # div_intriduce = div_value.find('div', 'p-name p-name-type-2')
            # div_intriduce = div_value.find('div', 'p-name p-name-type-2').find('a')
            # div_intriduce = div_value.find('div', 'p-name p-name-type-2').find('a').find('em')
            div_intriduce = div_value.find('div', 'p-name p-name-type-2').find('a').attrs['title']
            #评论数
            div_comment=div_value.find('div','p-commit').find('a').string
            ulist.append([div_price,div_comment,div_intriduce])
    return ulist
import re
def fillUnivlistRex(html):
    soup = BeautifulSoup(html, 'html.parser')
    soup.prettify()
    #     print()
    print(soup)
    trs=soup.find('ul','gl-warp clearfix').find_all('li','gl-item')
    ulist=[]
    plt=re.findall(r'class=\"p-price\">.*?</div>',html)
    for temp in plt:
        res=re.findall('/">*</i>',temp)
    for tr in trs:
        #将不是标签的数据过滤掉，最后一个黄山学院就不是标签数据
        if isinstance(tr,bs4.element.Tag):
            div_value=tr.find('div','gl-i-wrap')
            div_value.prettify()
            div_price=div_value.find('div','p-price').find('strong').find('i').string
            # 产品介绍
            # div_intriduce = div_value.find('div', 'p-name p-name-type-2')
            # div_intriduce = div_value.find('div', 'p-name p-name-type-2').find('a')
            # div_intriduce = div_value.find('div', 'p-name p-name-type-2').find('a').find('em')
            div_intriduce = div_value.find('div', 'p-name p-name-type-2').find('a').attrs['title']
            #评论数
            div_comment=div_value.find('div','p-commit').find('a').string
            ulist.append([div_price,div_comment,div_intriduce])
    return ulist

def getHtmlTextWebdriver(url):
    options = webdriver.Chrome()
    options.maximize_window()
    options.get(url)
    # options.find_element_by_id("kw").send_keys("Selenium2")
    # options.find_element_by_id("su").click()
    # res=options.get_cookies()
    # bs_val=BeautifulSoup(options.page_source)
    return options.page_source

def printUnivList(ulist,num):
    # print('共有{0}个学校参加排名'.format(str(len(ulist))))
    tplt = "{0:{3}^10}\t{1:{3}^10}\t{2:{3}^30}"
    print(tplt.format('价格','评论数','描述',chr(12288)))
    if num>len(ulist):
        num=len(ulist)
    for i in range(num):
        # print(ulist[i])
        #4是有4个字符，10是占用是个字符
        print(tplt.format(str(ulist[i][0]),str(ulist[i][1]),str(ulist[i][2])[:20],chr(12288)))


def main():
    uinfo = []
    # url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    url='https:////search.jd.com/Search?keyword=书包&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=书包&stock=1&page=9&s=241&click=0'
    html = getHtmlTextWebdriver(url)
    ulist=fillUnivlistRex(html=html)
    printUnivList(ulist=ulist,num=550)

if __name__=='__main__':
    main()


