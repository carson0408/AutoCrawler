# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawltosqlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义帖子的链接
    url = scrapy.Field()

    # 定义帖子的标题
    title = scrapy.Field()

    # 定义帖子的作者
    author = scrapy.Field()

    # 定义作者信息的链接
    authorlink = scrapy.Field()

    # 定义帖子回复
    reply = scrapy.Field()

    # 定义浏览情况
    scan = scrapy.Field()

    # 定义发布时间
    pubtime = scrapy.Field()

    # 定义最后回复时间
    lastreplytime = scrapy.Field()

    # 定义最后回复的作者
    endauthor = scrapy.Field()

