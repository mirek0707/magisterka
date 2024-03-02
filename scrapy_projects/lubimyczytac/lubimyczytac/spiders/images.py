import scrapy
import re


class ImagesSpider(scrapy.Spider):
    name = "images"
    allowed_domains = ["lubimyczytac.pl"]
    start_urls = ["https://lubimyczytac.pl/katalog?listId=booksFilteredList&rating[0]=0&rating[1]=10&publishedYear[0]=2024&publishedYear[1]=2024&catalogSortBy=ratings-desc&paginatorType=Standard"]
    curr_page_num = 1
    curr_year = 2024

    def parse(self, response):
        books = response.xpath(
            "//div[@class='authorAllBooks__single']/div/div[@class='col authorAllBooks__singleCenter authorAllBooks__singleCenter--list']/div/div/a[@class='authorAllBooks__singleTextTitle float-left']")
        for book in books:
            url = book.xpath(".//@href").get()

            yield response.follow(url=url, callback=self.parse_book)

        self.curr_page_num += 1
        max_page_num = response.xpath(
            "//div/div[@id='booksFilteredListPaginatorButton']/div/nav/ul/li[@class='paginationList__info']/span/text()").get()
        if (self.curr_page_num <= int(max_page_num)):
            next_page = self.start_urls[0] + "&page=" + str(self.curr_page_num)
            yield scrapy.Request(url=next_page, callback=self.parse)
        else:
            self.curr_page_num = 1
            if self.curr_year > 1963:
                self.start_urls[0] = self.start_urls[0].replace(
                    str(self.curr_year), str(self.curr_year - 1))
                self.curr_year -= 1
                yield scrapy.Request(url=self.start_urls[0], callback=self.parse)
            else:
                self.start_urls[0] = self.start_urls[0].replace(
                    str(self.curr_year), "1200", 1)
                self.start_urls[0] = self.start_urls[0].replace(
                    str(self.curr_year), str(self.curr_year - 1), 1)
                self.curr_year -= 1
                yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse_book(self, response):
        isbn = response.xpath(
            "normalize-space(.//div/div/div[@id='book-details']/dl/dt[text()=' ISBN:']/following-sibling::dd[1]/text())").get()
        isbn = isbn.replace("-", "")
        isbn = isbn.replace("x", "X")

        img_src = response.xpath(".//div/div/div/div/div/a/@href").get()

        pattern = r'^0+(X)?$'
        if not re.match(pattern, isbn) and isbn != "":
            yield {
                'isbn': isbn,
                'img_src': img_src
            }
