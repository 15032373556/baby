# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastItem(scrapy.Item):
    # 抓取 1.讲师姓名 2.讲师职称 3.讲师个人信息
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
