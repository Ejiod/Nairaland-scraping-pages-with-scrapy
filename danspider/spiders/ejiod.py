# -*- coding: utf-8 -*-
import scrapy


class EjiodSpider(scrapy.Spider):
    name = 'ejiod'
    allowed_domains = ['nairaland.com']
    start_urls = ['http://nairaland.com/']

    def parse(self, response):
        bees=response.xpath("//td[@class='featured w']")
        for be in bees:
            text = bees.xpath('.//a/b/text()').extract()
            href = bees.xpath('.//a/@href').extract()

            yield{
                'text':text,
                'href':href

            }

         