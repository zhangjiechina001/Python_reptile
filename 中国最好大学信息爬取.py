# 最好大学排名信息爬取
import requests
from bs4 import BeautifulSoup


def getHtmlText(url):
    kv = {'user-agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=kv, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('爬取错误')

import bs4
def fillUnivList(html):
    soup = BeautifulSoup(html, 'html.parser')
    soup.prettify()
    #     print()
    trs=soup.find_all('tr','bgfd')
    ulist=[]
    for tr in trs:
        #将不是标签的数据过滤掉，最后一个黄山学院就不是标签数据
        if isinstance(tr,bs4.element.Tag):
            # print(tr, '\n')
            td_rank=tr.find_all('td')
            ulist.append([td_rank[0].string,td_rank[1].string,td_rank[2].string,td_rank[3].string])
            # print(td_rank[0].string,td_rank[1].string,td_rank[2].string,td_rank[3].string)
            # ulist.append([])
    return ulist


def printUnivList(ulist,num):
    print('共有{0}个学校参加排名'.format(str(len(ulist))))
    if num>len(ulist):
        num=len(ulist)
    for i in range(num):
        # print(ulist[i])
        #4是有4个字符，10是占用是个字符
        tplt = "{0:{4}^10}\t{1:{4}^10}\t{2:{4}^10}\t{3:{4}^10}"
        print(tplt.format(str(ulist[i][0]),str(ulist[i][1]).replace('None','无'),str(ulist[i][2]),str(ulist[i][3]),chr(12288)))


def main():
    uinfo = []
    # url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    url='http://www.zuihaodaxue.com/BCSR/zhengzhixue2019.html'
    html = getHtmlText(url)
    ulist=fillUnivList(html=html)
    printUnivList(ulist=ulist,num=550)

if __name__=='__main__':
    main()