import scrapy
import xml.etree.ElementTree as ET


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["goodreads.com"]
    api_key = "xQXvrwOTLq7xonOLcjt2A"

    def start_requests(self):
        with open('../../isbns.txt', 'r') as file:
            isbn_list = file.readlines()

        for isbn in isbn_list:
            isbn = isbn.strip()
            url = f'https://www.goodreads.com/search/index.xml?key={self.api_key}&q={isbn}'
            yield scrapy.Request(url, callback=self.parse, meta={'q': isbn, 'key': self.api_key})

    def parse(self, response):
        xml_response = ET.fromstring(response.body)

        query = xml_response.find('.//search/query').text
        results = xml_response.find('.//results/work')

        if results is not None:
            average_rating = results.find('.//average_rating').text
            ratings_count = results.find('.//ratings_count').text
            author_name = results.find('.//author/name').text
            title = results.find('.//best_book/title').text
            publication_year = results.find(
                './/original_publication_year').text or ""
            publication_month = results.find(
                './/original_publication_month').text
            publication_day = results.find('.//original_publication_day').text

            publication_date = (publication_year+'-'+publication_month+'-' +
                                publication_day) if (publication_month and publication_day) else ''

            yield {
                'title': title,
                'author': author_name,
                'isbn': query,
                'rating_gr': average_rating,
                'ratings_gr_number': ratings_count,
                'release_date': publication_date,
                'release_year': publication_year
            }
