import scrapy


class ImagesSpider(scrapy.Spider):
    name = "images"
    allowed_domains = ["taniaksiazka.pl"]
    start_urls = ["https://www.taniaksiazka.pl/ksiazki-c-14141.html"]

    url_prefix = "https://www.taniaksiazka.pl"

    def parse(self, response):
        books = response.xpath("//section/div/div/article/ul/li")
        for book in books:
            url = book.xpath(".//div/div/div/div/div/div/h3/a/@href").get()
            yield response.follow(url=url, callback=self.parse_book)
        next_page = response.xpath(
            "//div[5]/section/div/div/article/div/ul/li[@class='next']/a/@href"
        ).get()
        yield scrapy.Request(url=self.url_prefix + next_page, callback=self.parse)

    def parse_book(self, response):
        img_src = response.xpath(
            "normalize-space(//div[5]/section/div[1]/form/fieldset/div/div/div/ul/li/a/@href)"
        ).get()
        isbn = response.xpath(
            "normalize-space(//div[5]/section/div[1]/div[2]/div[3]/article/div[2]/div/ul[1]/li[text()='ISBN: ']/strong/text())"
        ).get()

        if isbn != "":
            yield {"isbn": isbn, "img_src": img_src}
