# from: en
# to: zh
# query: cat
# transtype: realtime
# simple_means_flag: 3
# sign: 661701.982004
# token: 223c0d460a3e1417ca97feb683533ada
# domain: common

dat="""from: en
to: zh
query: dog
simple_means_flag: 3
sign: 871501.634748
token: 223c0d460a3e1417ca97feb683533ada
domain: common"""

import requests
import re
def str2dict(formstr):
    form = {}
    r = re.findall(r'(.*?):(.*?)\n', formstr)
    for i in r:
        form[i[0].strip()] = i[1].strip()
    return form

head="""Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
Connection: keep-alive
Content-Length: 135
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: BIDUPSID=A41F1AADF803EF20E05AB53D2002DAD0; PSTM=1618563722; BAIDUID=A41F1AADF803EF20921C4D37863F817F:FG=1; __yjs_duid=1_3aff4892e45dc91d12d7a911f51545491618576473168; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=k5FWDZRcm82aH44MlJLQU5lcjRTWGJxODlSR1V-cXpQZ3hJeXFsSnRoWG9LT2hnRUFBQUFBJCQAAAAAAAAAAAEAAAC7SfdAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOibwGDom8BgY; BDUSS_BFESS=k5FWDZRcm82aH44MlJLQU5lcjRTWGJxODlSR1V-cXpQZ3hJeXFsSnRoWG9LT2hnRUFBQUFBJCQAAAAAAAAAAAEAAAC7SfdAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOibwGDom8BgY; BAIDUID_BFESS=F429AFA68DBA255F053CD2A93CBE96FD:FG=1; BDRCVFR[n9IS1zhFc9f]=mk3SLVN4HKm; delPer=0; PSINO=2; H_PS_PSSID=26350; BA_HECTOR=012lag052g200k211r1gs8svb0q; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1640264708; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1640264713; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1639566868,1639567254,1640264688,1640264743; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1640265030; ab_sr=1.0.1_ODkxMzM3MzY3ZjI3ZWE2NWZlNmM4ZTIyNmQzMTRjZWZjNzI2MzgyYjc4MzJlZWM0YWI4ZDkyMTY3MDAwNmU0N2U1ZWZhYWEzNWJmZTFkN2FlMDU4MmQ4MGM4NzliMmE0ZmM2NTI1ZDVkNmRjYzdjNjExNDQwYTI3NjdmNjI5NzJmMGFhNDg2MmNmMDc5YjIxOTI3OTY5YjlhZTgxMDhiYzlmMjQ0YzI4N2JkNzM5YmNhOGQ4M2ZkMzI2Y2Y3MjZj; __yjs_st=2_ODk1MzI3YTFkZGM1OGM3NDE1MGE0Y2EwMTM1ZTAxYjEzOWFiMDE5MDM1MmVhNjQwNDU5ZDRiMzExYzZkNDMxNTdjMGQ2MzYwNzE5ZTg2MzlkNTA3M2Q2N2Y3NmE4ZGRkMDM0NzQ2MmYyNzU0N2ZkNTQ1OTYwZjMxZmEwYmE2YWVlYTc2M2M2Mjk1MDJmYjNhZGI5NzhhMmI1MzhmNjM3ZGUyYjk0ZjgzNTNhZTViYTRkZjg3ZjdhYzVmODVkYTgyYmE1NzZkOTI0NTU2YzAyNGE0ZjVjMzUwNzQxZTgwZmU0MGNlN2VhOGU5NGI1MWU2YzU5NmVkZjFkZDBjNTNmMV83XzVlZjA0OGI3
Host: fanyi.baidu.com
Origin: https://fanyi.baidu.com
Referer: https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"
sec-ch-ua-mobile: ?0
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36
X-Requested-With: XMLHttpRequest"""
#sug简单爬取
word=input("请输入要翻译的单词\n")
headers=str2dict(head)
data={
    'kw':word
}
html=requests.post(url="https://fanyi.baidu.com/sug",data=data,headers=headers).json()

print(html)

# data={
#     'from': 'en',
#     'to': 'zh',
#     'query': word,
#     'simple_means_flag': '3',
#     'sign': '871501.634748',
#     'token': '223c0d460a3e1417ca97feb683533ada'
# }