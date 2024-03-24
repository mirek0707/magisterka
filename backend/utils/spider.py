import requests
from bs4 import BeautifulSoup


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


def get_books_from_shelf(content):
    try:
        soup = BeautifulSoup(content, "html.parser")

        books = soup.find_all("a", class_="authorAllBooks__singleTextTitle float-left")
        books_links = ["https://lubimyczytac.pl" + book["href"] for book in books]
        return books_links

    except requests.exceptions.RequestException as e:
        print("Unable to scrap data:", e)
        return None
