# -*- coding: utf-8 -*-
import scrapy

from scrapy import Request

from crawltosql.items import CrawltosqlItem


class CrawlSpider(scrapy.Spider):
    name = 'crawl'
    allowed_domains = ['hupu.com']
    start_urls = ['https://bbs.hupu.com/vote']

    def parse(self, response):
        item = CrawltosqlItem()
        item["url"]=response.xpath("//a[@class='truetit']/@href").extract()
        item["title"]=response.xpath("//a[@class='truetit']/text()").extract()
        item["author"]=response.xpath("//a[@class='aulink']/text()").extract()
        item["authorlink"]=response.xpath("//a[@class='aulink']/@href").extract()
        #item["replyandscan"]
        #由于replyandscan元素中包含'\xa0',会出现报错，所以需要单独处理，将浏览情况与回复情况拆分
        t=response.xpath("//span[@class='ansour box']/text()").extract()
        reply=[]
        scan=[]
        for u in t:
            tmp=str(u).replace("\xa0","").split("/")
            if(tmp!=[]):
                reply.append(tmp[0])
                scan.append(tmp[1])
        item["reply"]=reply
        item["scan"]=scan

        item["pubtime"]=response.xpath("//div[@class='author box']//a[@style='color:#808080;cursor: initial; ']/text()").extract()
        item["lastreplytime"]=response.xpath("//div[@class='endreply box']/a/text()").extract()
        item["endauthor"]=response.xpath("//div[@class='endreply box']/span/text()").extract()

        yield item

        for i in range(2,21):
            url="https://bbs.hupu.com/vote-"+str(i)
            #通过yield返回Request，并指定要爬取的url和回调函数，从而实现自动爬取
            yield Request(url,callback=self.parse)

