#百度网页采集器

import requests
if __name__ == '__main__':
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
    }

    url='https://www.baidu.com/s'
    kw=input('enter a word')
    param={
        'wd':kw
    }
    response=requests.get(url=url,params=param,headers=headers)
    page_text=response.text
    fileName=kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功!!!')
