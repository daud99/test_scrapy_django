import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['www.imdb.com/']
    start_urls = ['https://www.imdb.com/title/tt0120737/?ref_=nv_sr_srsg_0/']

    def parse(self, response):
        title = response.xpath("//h1/text()").get()

        yield {
            'title': title,
            'source': 'source',
            'description': 'description',
            'reviews': 'reviews',
            'quotes': 'quotes'
        }
