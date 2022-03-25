#kfc点餐地址
import requests
import json


if __name__ == '__main__':
    word=input('enter a word')
    url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
    params={
        'op':'keyword'
    }
    data={'cname': '',
          'pid': '',
          'keyword': word,
          'pageIndex': '1',
          'pageSize':'10'}

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
    }

    response=requests.post(url=url,params=params,data=data,headers=headers)
    page_text=response.json()
    print(page_text)

