import json

# Lista przechowująca numery ISBN
isbn_numbers_set = set()

# Wczytaj dane z pierwszego pliku JSON
with open("./books.json", "r") as json_file:
    data1 = json.load(json_file)
    for book in data1:
        isbn = book.get("isbn")
        if isbn:
            isbn_numbers_set.add(isbn)

# Wczytaj dane z drugiego pliku JSON
with open("./scrapy_projects/lubimyczytac/books5.json", "r") as json_file:
    data2 = json.load(json_file)
    for book in data2:
        isbn = book.get("isbn")
        if isbn:
            isbn_numbers_set.add(isbn)

# Otwórz plik tekstowy w trybie zapisu
with open("isbns.txt", "w") as file:
    # Zapisz numery ISBN do pliku
    for isbn in isbn_numbers_set:
        file.write(isbn + "\n")  # Zapisz numer ISBN do pliku, każdy w nowej linii
