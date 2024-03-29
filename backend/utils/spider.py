import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime
from pyisbn import Isbn


def get_shelves(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        shelves_data = dict()

        shelves = soup.find_all("input", class_="filtr__itemCheckbox")
        for shelf in shelves:
            shelf_name = shelf["data-shelf-name"]
            shelf_value = shelf["value"]
            shelves_data[shelf_name] = shelf_value

        return shelves_data

    except requests.exceptions.RequestException as e:
        print("Unable to scrap data:", e)
        return None


def get_userId(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        uid = soup.find("input", id="objectId")

        return uid["value"]

    except requests.exceptions.RequestException as e:
        print("Unable to scrap data:", e)
        return None


def get_book_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print("Unable to scrap data:", e)
        return None

    try:
        title = str(soup.find("h1", class_="book__title").get_text()).strip()
        author = str(
            soup.find("a", class_="link-name d-inline-block").get_text()
        ).strip()
        isbn = str(soup.find(string=" ISBN:").findNext("dd").contents[0]).strip()
        isbn = isbn.replace("-", "")
        isbn = isbn.replace("x", "X")
    except AttributeError:
        return

    try:
        isbn_obj = Isbn(isbn)
        if not isbn_obj.validate():
            raise ValueError("ISBN is not valid")
    except ValueError:
        return

    try:
        pages = int(soup.find(string=" Liczba stron:").findNext("dd").contents[0])
    except AttributeError:
        pages = None

    try:
        publisher = str(
            (
                soup.find("span", class_="book__txt d-block d-xs-none mt-2")
                .findChildren("a")[0]
                .get_text()
            )
        ).strip()
    except AttributeError:
        publisher = ""

    try:
        original_title = (
            str(soup.find(string=" Tytuł oryginału:").findNext("dd").contents[0])
        ).strip()
    except AttributeError:
        original_title = ""

    try:
        release_date = datetime.fromisoformat(
            str(soup.find(string=" Data wydania:").findNext("dd").contents[0]).strip()
        ).replace(hour=12, minute=00)
    except AttributeError:
        release_date = None

    try:
        polish_release_date = datetime.fromisoformat(
            str(
                soup.find(string=" Data 1. wyd. pol.:").findNext("dd").contents[0]
            ).strip()
        ).replace(hour=12, minute=00)
    except AttributeError:
        polish_release_date = None

    try:
        rating_lc = float(
            soup.find("div", class_="rating-value", attrs={"data-toggle": "tooltip"})
            .findChildren("span")[0]
            .get_text()
            .replace(",", ".")
        )
        ratings_lc_number = int(
            re.findall(
                r"\d+",
                str(soup.findAll("section", class_="rating rating--legacy")).split(
                    "</span> / 10</div>"
                )[-1],
            )[0]
        )
    except AttributeError:
        rating_lc = 0
        ratings_lc_number = 0

    try:
        description_list = soup.find(
            "div",
            id="book-description",
        ).findAll("p")
        description_list = [str(i.get_text()) for i in description_list]
        description = "\n".join(description_list)
    except AttributeError:
        description = ""

    try:
        genre = str(
            soup.find("div", class_="col-12 col-lg-6 book__desc")
            .find("a", class_="book__category d-sm-block d-none")
            .get_text()
        ).strip()
    except AttributeError:
        genre = ""

    try:
        img_src = str(soup.find("a", id="js-lightboxCover")["href"])
    except AttributeError:
        img_src = ""

    return {
        "title": title,
        "author": author,
        "isbn": isbn,
        "pages": pages,
        "publisher": publisher,
        "original_title": original_title,
        "release_date": release_date,
        "polish_release_date": polish_release_date,
        "rating_lc": rating_lc,
        "ratings_lc_number": ratings_lc_number,
        "description": description,
        "genre": genre,
        "img_src": img_src,
    }


def get_books_from_shelf(content):
    try:
        soup = BeautifulSoup(content, "html.parser")

        books = soup.find_all("a", class_="authorAllBooks__singleTextTitle float-left")
        books_links = ["https://lubimyczytac.pl" + book["href"] for book in books]
        return books_links

    except requests.exceptions.RequestException as e:
        print("Unable to scrap data:", e)
        return None
