# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NamesItem(scrapy.Item):
    # define the fields for your item here like:
    first_name = scrapy.Field()
    f_url = scrapy.Field()
    name = scrapy.Field()
    name_url = scrapy.Field()
    detail = scrapy.Field()
