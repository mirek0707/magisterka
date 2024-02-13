import scrapy
import re


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["lubimyczytac.pl"]
    start_urls = ["https://lubimyczytac.pl/katalog?listId=booksFilteredList&rating[0]=0&rating[1]=10&publishedYear[0]=2024&publishedYear[1]=2024&catalogSortBy=ratings-desc&paginatorType=Standard"]
    curr_page_num = 1
    curr_year = 2024

    def parse(self, response):
        books = response.xpath("//div[@class='authorAllBooks__single']/div/div[@class='col authorAllBooks__singleCenter authorAllBooks__singleCenter--list']/div/div/a[@class='authorAllBooks__singleTextTitle float-left']")
        for book in books:
            url = book.xpath(".//@href").get()

            yield response.follow(url=url, callback = self.parse_book)
        
        self.curr_page_num += 1
        max_page_num = response.xpath("//div/div[@id='booksFilteredListPaginatorButton']/div/nav/ul/li[@class='paginationList__info']/span/text()").get()
        if (self.curr_page_num <= int(max_page_num)):
            next_page = self.start_urls[0] + "&page=" + str(self.curr_page_num)
            yield scrapy.Request(url=next_page, callback=self.parse)
        else:
            self.curr_page_num = 1
            if self.curr_year > 1963:
                self.start_urls[0] = self.start_urls[0].replace(str(self.curr_year), str(self.curr_year - 1))
                self.curr_year -=1
                yield scrapy.Request(url=self.start_urls[0], callback=self.parse)
            else:
                self.start_urls[0] = self.start_urls[0].replace(str(self.curr_year), "1200", 1)
                self.start_urls[0] = self.start_urls[0].replace(str(self.curr_year), str(self.curr_year - 1), 1)
                self.curr_year -=1
                yield scrapy.Request(url=self.start_urls[0], callback=self.parse)


    def parse_book(self, response):
        title = response.xpath("normalize-space(.//div/div[@class='title-container relative']/h1/text())").get()
        author = response.xpath("normalize-space(.//div/div/span/a[@class='link-name d-inline-block']/text())").get()
        isbn = response.xpath("normalize-space(.//div/div/div[@id='book-details']/dl/dt[text()=' ISBN:']/following-sibling::dd[1]/text())").get()
        isbn = isbn.replace("-", "")
        isbn = isbn.replace("x", "X")
        pages = response.xpath("normalize-space(.//div/div/div[@id='book-details']/dl/dt[text()=' Liczba stron:']/following-sibling::dd[1]/text())").get()
        publisher = response.xpath("normalize-space(.//div/div/span[@class='book__txt d-block d-xs-none mt-2 ']/a/text())").get()
        original_title = response.xpath("normalize-space(.//div/div/div[@id='book-details']/dl/dt[text()=' Tytuł oryginału:']/following-sibling::dd[1]/text())").get()
        release_date = response.xpath("normalize-space(.//div/div/div[@id='book-details']/dl/dt[text()=' Data wydania:']/following-sibling::dd[1]/text())").get()
        polish_release_date = response.xpath("normalize-space(.//div/div/div[@id='book-details']/dl/dt[@aria-label='Data pierwszego wydania polskiego']/following-sibling::dd[1]/text())").get()
        rating = response.xpath("normalize-space(.//div/div/section/div/div[@class='rating-value']/span/text())").get()
        ratings_number_text = response.xpath("normalize-space(.//div/div/section/div/div/section[@class='rating rating--legacy']/text()[2])").get()
        ratings_number = re.findall(r'\d+', ratings_number_text)[0]
        description_list = response.xpath("(//div[@id='book-description']/div/p/text())").getall()
        description = '\n'.join(map(str, description_list))
        
        pattern = r'^0+(X)?$'
        if not re.match(pattern, isbn) and isbn != "":
            yield {
                'title' : title,
                'author': author,
                'isbn': isbn,
                'pages': pages,
                'publisher': publisher,
                'original_title': original_title,
                'release_date': release_date,
                'polish_release_date': polish_release_date,
                'rating': rating,
                'ratings_number': ratings_number,
                'description': description
            }
