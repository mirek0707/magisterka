import scrapy
import time
import xml.etree.ElementTree as ET
from scrapy.spidermiddlewares.httperror import HttpError


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["goodreads.com"]
    api_key = "xQXvrwOTLq7xonOLcjt2A"
    use_proxy = False
    proxy_index = 0
    proxy_pool = [
        # 'https://3.112.35.208:3128',  # działało kiedys
        # 'https://103.166.141.74:20074',  # działa ale wolno
        "https://185.165.46.208:3128",  # działa
        "https://185.217.136.67:1337",  # działa
        "https://139.180.39.201:8080",  # działa
        "https://35.185.196.38:3128",  # działa
        "https://140.238.245.116:8100",  # działa troche wolno
        "https://189.240.60.166:9090",  # działa troche wolno
        "https://189.240.60.169:9090",  # działa troche wolno
    ]

    def start_requests(self):
        with open("../../isbns.txt", "r") as file:
            isbn_list = file.readlines()

        for isbn in isbn_list:
            isbn = isbn.strip()
            url = f"https://www.goodreads.com/search/index.xml?key={self.api_key}&q={isbn}"

            # proxy run
            # yield scrapy.Request(url, callback=self.parse, errback=self.errback,  meta={'q': isbn, 'key': self.api_key, 'proxy': self.proxy_pool[self.proxy_index % len(self.proxy_pool)]})

            # no proxy run
            yield scrapy.Request(
                url, callback=self.parse, meta={"q": isbn, "key": self.api_key}
            )

    def parse(self, response):
        xml_response = ET.fromstring(response.body)

        query = xml_response.find(".//search/query").text
        results = xml_response.find(".//results/work")

        if results is not None:
            average_rating = results.find(".//average_rating").text
            ratings_count = results.find(".//ratings_count").text
            author_name = results.find(".//author/name").text
            title = results.find(".//best_book/title").text
            publication_year = results.find(".//original_publication_year").text or ""
            publication_month = results.find(".//original_publication_month").text
            publication_day = results.find(".//original_publication_day").text

            publication_date = (
                (publication_year + "-" + publication_month + "-" + publication_day)
                if (publication_month and publication_day)
                else ""
            )

            yield {
                "title": title,
                "author": author_name,
                "isbn": query,
                "rating_gr": average_rating,
                "ratings_gr_number": ratings_count,
                "release_date": publication_date,
                "release_year": publication_year,
            }

    def errback(self, failure):
        self.logger.error(repr(failure))
        request = failure.request

        if (
            request.meta["proxy"]
            == self.proxy_pool[self.proxy_index % len(self.proxy_pool)]
        ):
            self.proxy_index += 1
            if self.proxy_index % len(self.proxy_pool) == 0:
                self.logger.error("sleep time :3")
                time.sleep(5 * 60)  # 5 minutes

        self.logger.error(
            "!!!!!!!!!!!!!!!!!%s - Changing proxy to %d",
            request.url,
            self.proxy_index % len(self.proxy_pool),
        )
        yield scrapy.Request(
            request.url,
            callback=self.parse,
            errback=self.errback,
            meta={
                "q": request.url.split("&q=")[1],
                "key": self.api_key,
                "proxy": self.proxy_pool[self.proxy_index % len(self.proxy_pool)],
            },
        )
