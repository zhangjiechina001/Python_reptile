import requests
from bs4 import BeautifulSoup
import traceback
import re
def getHTMLtext(url):
    kv = {'user-agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=kv, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('爬取错误')
    return ''
# [s][hz]\d{6}
def getStockList(stockURL):
    return

def getStockInfo(lst,stockURL,fpath):
    return
def printList(ulist):
    return

def main():
    stock_list_url='http://quote.eastmoney.com/center/gridlist.html#hs_a_board'
    stockj_info_url='https://gupiao.baidu.com/stock/'
    output_file='BaiduStockInfo.txt'
    #获取股票列表
    slist=getStockList(stock_list_url)
    infoList=getStockInfo(stockj_info_url,output_file)

if __name__=='__mian__':
    main()
