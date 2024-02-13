import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["taniaksiazka.pl"]
    start_urls = ["https://www.taniaksiazka.pl/ksiazki-c-14141.html"]

    url_prefix = "https://www.taniaksiazka.pl"

    def parse(self, response):
        books = response.xpath("//section/div/div/article/ul/li")
        for book in books:
            url = book.xpath(".//div/div/div/div/div/div/h3/a/@href").get()
            yield response.follow(url=url, callback=self.parse_book)
        next_page = response.xpath(
            "//div[5]/section/div/div/article/div/ul/li[@class='next']/a/@href").get()
        yield scrapy.Request(url=self.url_prefix+next_page, callback=self.parse)

    def parse_book(self, response):
        title = response.xpath(
            "normalize-space(//div[5]/section/div[1]/form/fieldset/div[2]/h1/span/text())").get()
        author = response.xpath(
            "normalize-space(//div[5]/section/div[1]/form/fieldset/div[2]/div[1]/h2/a/text())").get()
        isbn = response.xpath(
            "normalize-space(//div[5]/section/div[1]/div[2]/div[3]/article/div[2]/div/ul[1]/li[text()='ISBN: ']/strong/text())").get()
        pages = response.xpath(
            "normalize-space(//div[5]/section/div[1]/form/fieldset/div/div/div/div/div[text()='Ilość stron']/following-sibling::div/text())").get()
        release_date = response.xpath(
            "normalize-space(//div[5]/section/div[1]/div[2]/div[3]/article/div[2]/div/ul[1]/li[text()='Rok wydania: ']/strong/text())").get()
        publisher = response.xpath(
            "normalize-space(//div[5]/section/div[1]/div[2]/div[3]/article/div[2]/div/ul[1]/li/a/span[text()='Wydawnictwo']/following-sibling::strong/text())").get()
        rating = response.xpath(
            "normalize-space(//div/section/div/form/fieldset/div/div/div/strong[1]/text())").get() or '0.0'
        ratings_number = response.xpath(
            "normalize-space(//div/section/div/form/fieldset/div/div/div/strong[2]/text())").get() or '0'

        if isbn != '':
            yield {
                'title': title,
                'author': author,
                'isbn': isbn,
                'pages': pages,
                'publisher': publisher,
                'release_year': release_date,
                'rating': rating,
                'ratings_number': ratings_number
            }
