# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/random']

    def parse(self, response):
        self.log('I just visited' + response.url)
        yield {
            'author_name' : response.css('small.author::text').extract(),
            'author_name1' : response.xpath('//div/div[2]/div/div/span[2]').extract(),
            'text' : response.css('span.text::text').extract(),
            'tags' : response.css('a.tag::text').extract,
            'tag_link' : response.css('a.tag::attr(href)').extract,
            # use xpath to iterate to a particular div using progressive approach.
            'tag_element' : response.xpath('//div/div[2]/div/div/span[2]/a[@href]')[0].extract(),
            # use xpath to find elements with a particular id, class, attribute
            'span_element' : response.xpath('//span[@class="sh-red"]/text()').extract(),
            #xpath contains method.
            'span_element': response.xpath('//span[contains(@class, "text")]/text()').extract(),

        }