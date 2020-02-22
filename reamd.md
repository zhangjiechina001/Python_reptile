requests.request(method,url,**kwargs)

**kwargs:控制访问的参数，均为可选项

1.data:字典，data={'key1':'value1','key2':'value2'}
2.json:作为request内容
3.headers：字典，HTTP定制头headers={'user-agent':'Chrom/10'},模拟任何想模拟的浏览器
4.cookies:
5.auth:元组
6.files:字典，传输文件
fs={'file':open('data.xls','rb')}
r=requests.request('POST','http://python123.io/ws',files=fs)
7.proxies:字典类型，设定访问代理服务器，也可以增加登陆认证