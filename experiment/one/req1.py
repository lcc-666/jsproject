import requests
from lxml import etree

url = "https://news.sxau.edu.cn/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50 "
}
req = requests.get(url, headers=headers, timeout=2)
req.encoding = req.apparent_encoding
tree = etree.HTML(req.text)
news = tree.xpath("/html/body/div[4]/div[1]/div[3]/ul/li/a/@title")
print("学校新闻")
for item in news:
    print(item)

notice=tree.xpath("/html/body/div[6]/div/div[1]/ul/li/a/@title")
print("通知")
for item in notice:
    print(item)

url = "https://news.sxau.edu.cn/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50 "
}
req = requests.get(url, headers=headers, timeout=2)
req.encoding = req.apparent_encoding
tree = etree.HTML(req.text)

