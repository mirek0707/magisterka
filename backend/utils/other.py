from fastapi import UploadFile
from pandas import read_csv


def merge_values(value1, value2):
    if value1 is None and value2 is None:
        return None

    if value1 is None:
        return value2

    if value2 is None:
        return value1

    if isinstance(value1, list):
        set_result = set(value1)
    else:
        set_result = {value1}

    if isinstance(value2, str):
        set_result.add(value2)
    elif isinstance(value2, list):
        set_result.update(value2)

    if len(set_result) == 1:
        return set_result.pop()
    else:
        return list(set_result)


def validate_csv_file(file: UploadFile):
    if not file.content_type in ["text/csv", "application/vnd.ms-excel"]:
        return False

    required_columns = [
        "Book Id",
        "Title",
        "Author",
        "Author l-f",
        "Additional Authors",
        "ISBN",
        "ISBN13",
        "My Rating",
        "Average Rating",
        "Publisher",
        "Binding",
        "Number of Pages",
        "Year Published",
        "Original Publication Year",
        "Date Read",
        "Date Added",
        "Bookshelves",
        "Bookshelves with positions",
        "Exclusive Shelf",
        "My Review",
        "Spoiler",
        "Private Notes",
        "Read Count",
        "Owned Copies",
    ]
    df = read_csv(file.file)
    return all(column in df.columns for column in required_columns)


def clean_isbn(isbn):
    return isbn.replace("=", "").replace('"', "")


def clean_title(title):
    if "(" not in title:
        return title
    else:
        return title.split("(")[0].strip()
