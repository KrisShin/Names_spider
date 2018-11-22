# -*- coding: utf-8 -*-
'''
Author: Kris Shin
Edit Time: 18-11-11 14:57:26
'''

from scrapy import Spider, Request

from names.items import NamesItem


class NameSpider(Spider):
    name = 'name'
    allowed_domains = ['resgain.net']
    start_urls = ['http://www.resgain.net/xmdq.html']

    def parse(self, response):
        fnames = response.xpath('//div[@class="row"]//div[2]//a')[:-1]
        for fname in fnames:
            name = NamesItem()
            name['first_name'] = fname.xpath(
                './text()').extract_first().replace('姓名字大全', '')
            name['f_url'] = 'http:' + fname.xpath('./@href').extract_first()
            for i in range(11):
                yield Request(
                    url=name['f_url'][:-5] + '_' + str(1) + '.html',
                    meta={'name': name},
                    callback=self.parse_names,
                    dont_filter=True)

    def parse_names(self, response):
        # print(response.text)
        names = response.selector.xpath('//div[3]/div[2]/div[1]/div/a')
        name = response.meta['name']
        for nm in names:
            name['name'] = nm.xpath('./text()').extract_first()
            detail_url = name['f_url'].split('name_list')[0] + nm.xpath(
                './@href').extract_first()[1:]
            name['name_url'] = detail_url
            yield Request(
                url=detail_url,
                meta={'name': name},
                callback=self.parse_detail)

    def parse_detail(self, response):
        name = response.meta['name']
        detail = response.selector.xpath(
            '/html/body/div[2]/div/div[4]/div[1]/div[1]/div[2]/strong/text()'
        ).extract_first()
        name['detail'] = detail
        yield name
