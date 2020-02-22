'''
标签树的下行遍历
.contents 子节点列表
.children 子节点迭代类型
.descenddants 子孙节点的迭代类型
标签树的上行遍历
.parent 节点的父亲节点
.parents 节点先辈的迭代类型，用于循环遍历先辈节点
'''
import requests
from bs4 import BeautifulSoup
demo=requests.get('http://python123.io/ws/demo.html').text
soup=BeautifulSoup(demo,'html.parser')
print(soup)
# print(soup.head,soup.head.contents,soup.body.contents)
# print('parents:',soup.html.parent)
# print(soup.a.next_sibling.next_sibling)
print(soup.prettify())