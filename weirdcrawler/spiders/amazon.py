import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon-spider"
    search_urls = 'https://www.amazon.in/s/ref=nb_sb_noss'
    start_urls = ['https://www.amazon.in']

    def parse(self, response):
        data = {
            'url': 'search - alias = aps',
            'field - keywords': 'watch',
        }
        yield scrapy.FormRequest(url=self.search_urls,
                                 formdata=data, callback=self.parse_quotes)

    def parse_quotes(self, response):
            print(response.text)