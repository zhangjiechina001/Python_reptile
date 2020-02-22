import requests
import os
path='abc.jpg'
url='http://img8.zol.com.cn/bbs/upload/19571/19570481.jpg'
r=requests.get(url)
print(r.status_code)
with open(path,'wb') as f:
    f.write(r.content)
f.close()

def get_pic(url,root):
    path=root+url.split('/')[-1]
    try:
        r = requests.get(url)
        print(r.status_code)
        r.raise_for_status()
        if not os.path.exists(root):
            os.mkdir(root)
        #是否存在文件
        if not os.path.exists(path):
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print('文件保存成功')
        else:
            print('文件已存在')
    except:
        print('爬取失败')

if __name__=='__main__':
    # path = 'abc.jpg'
    url = 'http://pic41.nipic.com/20140601/18681759_143805185000_2.jpg'
    root='pics//'
    get_pic(url,root)
