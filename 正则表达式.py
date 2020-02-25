# 正则表达式，简洁表达一组字符串的表达式
#正则表达式的语法，
'''

'''
import re
#后面重复四个
research=re.search(r'[1-9]\d{2}','BIT 907234')
print(research.group(0))

match=re.match(r'[1-9]\d{2}','907234 BIT')
print(match.group(0))

ls=re.findall(r'[1-9]\d{5}','BIT1000281 TSU100235')
print(ls)

split=re.split(r'[1-9]\d{5}','BIT1000281 TSU100235')
print(split)
#先将陪结果展示，后面剩下的单独展示
max_split=re.split(r'[1-9]\d{5}','BIT1000281 TSU100235',maxsplit=1)
print(max_split)

#以PY开头N结尾，中间有若干个字符串,默认采用匹配最长的子串
match=re.search(r'PY.*N','PYYYYANBNCNDN  PYQAN')
result=match.group(0)
print(result)
