import requests
from lxml import etree

url='http://xsjwxt.sxau.edu.cn:7872/img/captcha.jpg'

headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
}
cookie=requests.session()
img=cookie.get(url=url,headers=headers).content

with open('img.jpg','wb') as fp:
    fp.write(img)


yzm=input('请人工输入验证码')
xt_url='http://xsjwxt.sxau.edu.cn:7872/j_spring_security_check'
data={
    'j_username': '20190100702',
    'j_password': '30bfc136822f7e4106ee580972779e0e',
    'j_captcha': yzm
}

response=cookie.post(url=xt_url,data=data,headers=headers)

with open('jww.html','w',encoding='utf-8') as fp:
    fp.write(response.text)