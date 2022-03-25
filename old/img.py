#图片爬取样例
import requests

if __name__ == '__main__':
    url='https://img.lianzhixiu.com/uploads/allimg/160106/9-160106204243.jpg'
    img=requests.get(url=url).content
    with open('./test.jpg','wb') as fp:
        fp.write(img)