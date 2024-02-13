import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["taniaksiazka.pl"]
    start_urls = ["https://taniaksiazka.pl"]

    def parse(self, response):
        pass
