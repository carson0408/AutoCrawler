# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json


class AutocrawlPipeline(object):
    def __init__(self):
        #代码移植时注意改写
        self.file=codecs.open("../autocrawl/data.json","wb",encoding="utf-8")
    def process_item(self, item, spider):
        for j in range(len(item["url"])):
            url = "https://bbs.hupu.com"+item["url"][j]
            title=item["title"][j]
            author=item["author"][j]
            authorlink=item["authorlink"][j]
            reply=item["reply"][j]
            scan=item["scan"][j]
            pubtime=item["pubtime"][j]
            lastreplytime=item["lastreplytime"][j]
            endauthor=item["endauthor"][j]
            oneitem={"url":url,"title":title,"author":author,"authorlink":authorlink,"reply":reply,"scan":scan,
                     "pubtime":pubtime,"lastreplytime":lastreplytime,"endauthor":endauthor}
            i = json.dumps(oneitem, ensure_ascii=False)
            # 换行
            line = i + '\n'
            print(line)  # 调试
            self.file.write(line)
        return item
    def close_spider(self,spider):
        self.file.close()
