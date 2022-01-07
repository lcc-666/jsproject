import requests
from lxml import etree

if __name__ == '__main__':
    url='https://ty.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
    }
    page_text=requests.get(url=url,headers=headers).text

    tree=etree.HTML(page_text)
    div_list=tree.xpath("//div[@class='property']")
    fp=open('./58tongc.txt','w',encoding='utf-8')
    for li in div_list:
        title=li.xpath('.//div[@class="property-content-title"]/h3/text()')[0]
        fp.write(title+'\n')