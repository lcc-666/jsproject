import requests
import random
import time
from hashlib import md5
import re

def str2dict(formstr):
    form = {}
    r = re.findall(r'(.*?):(.*?)\n', formstr)
    for i in r:
        form[i[0].strip()] = i[1].strip()
    return form

head="""Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Connection: keep-alive
Content-Length: 240
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: OUTFOX_SEARCH_USER_ID="1468215353@10.108.160.19"; OUTFOX_SEARCH_USER_ID_NCOO=1938496365.1781125; JSESSIONID=aaa7TnWM3oTYT4Jd9uL3x; ___rl__test__cookies=1640230027726
Host: fanyi.youdao.com
Origin: https://fanyi.youdao.com
Referer: https://fanyi.youdao.com/
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62
X-Requested-With: XMLHttpRequest"""


headers=str2dict(head)
salt=str(int(time.time()*10000))+str(random.randint(0,9))
lts=str(int(time.time()*10000))
word=input("请输入要翻译的单词")
str_="fanyideskweb" + word + salt + "Y2FYu%TNSbMCxc3t2u^XT"
md=md5()
md.update(str_.encode())
sign=md.hexdigest()

data={
    'i': word,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'lts': lts,
    'bv': '2632875b568a3baf568a14dddf2c8f7f',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web'}
html=requests.post(url="https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule",data=data,headers=headers).json()

print(html["translateResult"][0][0]["tgt"])