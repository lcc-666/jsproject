#豆瓣电影数据获取
import requests
import json
import re

def str2dict(formstr):
    form = {}
    r = re.findall(r'(.*?):(.*?)\n', formstr)
    for i in r:
        form[i[0].strip()] = i[1].strip()
    return form

if __name__ == '__main__':
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
    }
    url='https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20'
    }
    response=requests.get(url=url,params=param,headers=headers)

    list_data=response.json()

    fp=open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
    print('over!!!')