import scrapy


class LightparsSpider(scrapy.Spider):
    name = "lightpars"
    allowed_domains = ["vseinstrumenti.ru"]
    start_urls = ["https://vseinstrumenti.ru"]

    def parse(self, response):
        pass
