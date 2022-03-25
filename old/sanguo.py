#三国演绎信息抓取
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text=requests.get(url=url,headers=headers).content
    soup=BeautifulSoup(page_text,'lxml')
    li_list=soup.select('.book-mulu > ul > li')
    fp=open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title=li.a.text
        detail_url='http://www.shicimingju.com'+li.a['href']
        detail_page_text=requests.get(url=detail_url,headers=headers).content
        detail_soup=BeautifulSoup(detail_page_text,'lxml')
        div_tag=detail_soup.find('div',class_='chapter_content')
        content=div_tag.text
        fp.write(title+":"+content+'\n')
        print(title,'success')


