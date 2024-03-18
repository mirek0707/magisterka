import scrapy
import json
from datetime import datetime
from dateutil import parser
from dateutil.parser import ParserError


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["openlibrary.org"]
    curr_isbn_index = 0
    isbn_list = []

    def start_requests(self):

        with open("../../isbns.txt", "r") as file:
            self.isbn_list = file.readlines()

        isbn = self.isbn_list[0].strip()
        url = f"http://openlibrary.org/api/volumes/brief/isbn/{isbn}.json"
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        resp = json.loads(response.body)
        if resp:
            records = resp.get("records", {})
            matching_keys = [key for key in records.keys() if key.startswith("/books/")]
            book = records.get(matching_keys[0], {})
            book_data = book.get("data")

            authors = book_data.get("authors")
            authors_list = []
            if authors:
                for author in authors:
                    if "," in author["name"]:
                        authors_list += author["name"].split(",")
                    else:
                        authors_list.append(author["name"])
            for author in authors_list:
                author = author.strip()

            publishers = book_data.get("publishers")
            publishers_list = []
            if publishers:
                for publisher in publishers:
                    publishers_list.append(publisher["name"])

            release_year = ""
            release_date = ""
            date = book.get("publishDates")[0]

            release_year = ""
            release_date = ""

            if date:
                try:
                    date_object = parser.parse(date)

                    release_year = date_object.strftime("%Y")
                    release_date = date_object.strftime("%Y-%m-%d")
                except ParserError:
                    pass

            yield {
                "isbn": self.isbn_list[self.curr_isbn_index].strip(),
                "title": book_data.get("title"),
                "release_year": release_year,
                "release_date": release_date,
                "author": (
                    authors_list[0]
                    if len(authors_list) == 1
                    else "" if len(authors_list) == 0 else authors_list
                ),
                "pages": (
                    str(book_data.get("number_of_pages"))
                    if book_data.get("number_of_pages") is not None
                    else ""
                ),
                "publisher": (
                    publishers_list[0]
                    if len(publishers_list) == 1
                    else "" if len(publishers_list) == 0 else publishers_list
                ),
            }
        self.curr_isbn_index += 1
        if self.curr_isbn_index < len(self.isbn_list):
            isbn = self.isbn_list[self.curr_isbn_index].strip()
            url = f"http://openlibrary.org/api/volumes/brief/isbn/{isbn}.json"
            yield scrapy.Request(url, callback=self.parse)
