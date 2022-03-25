import scrapy
from selenium import webdriver
from ..items import WangyiproItem

class wangyiproSpider(scrapy.Spider):
    name = 'wangyi'
    start_urls = ['https://news.163.com/']
    models_urls=[]
    def __init__(self):
        self.bro=webdriver.Chrome()

    def parse(self, response):
        li_list=response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        alist=[3,4,6,7,8]
        for index in alist:
            model_url=li_list[index].xpath('./a/@href').extract_first()
            self.models_urls.append(model_url)
        for url in self.models_urls:
            yield scrapy.Request(url=url,callback=self.parse_model)

    def parse_model(self,response):
        div_list=response.xpath('/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title=div.xpath('./div/div[1]/h3/a/text()').extract_first()
            item=WangyiproItem()
            item['title']=title
            new_detial_url=div.xpath('./div/div[1]/h3/a/@href').extract_first()
            yield scrapy.Request(url=new_detial_url,callback=self.parse_detail,meta={'item':item})

    def parse_detail(self,response):
        content=response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content=''.join(content)
        item=response.meta['item']
        item['content']=content
        yield item

    def closed(self,spider):
        self.bro.quit()




