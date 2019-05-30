# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql

class CrawltosqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="mydata")
    def process_item(self, item, spider):
        mylen = min(len(item["url"]),len(item["title"]),len(item["author"]),len(item["reply"]),len(item["scan"]),len(item["pubtime"]),len(item["lastreplytime"]),len(item["endauthor"]))
        for j in range(mylen):
            url = "https://bbs.hupu.com"+item["url"][j]
            title=item["title"][j]
            author=item["author"][j]
            authorlink=item["authorlink"][j]
            reply=item["reply"][j]
            scan=item["scan"][j]
            pubtime=item["pubtime"][j]
            lastreplytime=item["lastreplytime"][j]
            endauthor=item["endauthor"][j]
            #构造对应的sql语句，实现获取列的对应的数据插入到数据库中
            sql="insert into data(url,title,author,authorlink,reply,scan,pubtime,lastreplytime,endauthor) VALUES('"+url+"','"+title+"','"+author+"','"+authorlink+"','"+reply+"','"+scan+"','"+pubtime+"','"+lastreplytime+"','"+endauthor+"')"
            #通过query实现执行对应的sql语句
            self.conn.query(sql)
            self.conn.commit()


        return item
    def close_spider(self,spider):
        self.conn.close()
