from pydantic import ConfigDict, BaseModel, Field, HttpUrl
from typing import Optional
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator, field_validator
from datetime import datetime
from pyisbn import Isbn

PyObjectId = Annotated[str, BeforeValidator(str)]


class CreateBookModel(BaseModel):
    """
    Container for a create book request.
    """

    title: str = Field(...)
    author: str | list[str] | None = Field(...)
    pages: int | None = Field(...)
    isbn: str = Field(...)
    publisher: str | None = Field(...)
    original_title: str | None = Field(...)
    release_date: datetime | None = Field(...)
    release_year: int | None = Field(...)
    polish_release_date: datetime | None = Field(...)
    img_src: HttpUrl | list[HttpUrl] | str = Field(...)
    description: str | None = Field(...)
    genre: str | None = Field(...)

    @field_validator('isbn')
    @classmethod
    def validate_isbn(cls, isbn: str) -> str:
        isbn_obj = Isbn(isbn)
        if not isbn_obj.validate():
            raise ValueError('ISBN is not valid')

        return isbn

    @field_validator('pages')
    @classmethod
    def validate_pages(cls, pages: int) -> int:
        if pages <= 0:
            raise ValueError('Number of pages is not valid')
        return pages

    @field_validator("img_src")
    def validate_image_url(cls, img_src: HttpUrl | list[HttpUrl]):
        if img_src is not None:
            if type(img_src) is list:
                for url in img_src:
                    path = url.path
                    if not path.endswith((".jpg", ".jpeg", ".png", ".gif")):
                        raise ValueError(
                            "The URL must lead to an image (jpg, jpeg, png, or gif)")
            else:
                if img_src == "":
                    return img_src
                path = img_src.path
                if not path.endswith((".jpg", ".jpeg", ".png", ".gif")):
                    raise ValueError(
                        "The URL must lead to an image (jpg, jpeg, png, or gif)")
        return img_src

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "title": "W grze",
                "author": [
                    "Jerzy Brzęczek",
                    "Małgorzata Domagalik"
                ],
                "pages": 352,
                "isbn": "9788328075337",
                "publisher": "W.A.B. / GW Foksal",
                "original_title": "",
                "release_date": "2020-09-30T20:00:00",
                "release_year": 2020,
                "polish_release_date": "2020-09-30T20:00:00",
                "img_src": [
                    "https://bigimg.taniaksiazka.pl/images/popups/5B0/9788328075337.jpg",
                    "https://s.lubimyczytac.pl/upload/books/4941000/4941963/847365-352x500.jpg"
                ],
                "description": " Jego pojawienie się w roli selekcjonera polskiej reperentacji w 2018 roku wywołało niespotykaną dotąd w naszych mediach burzę. Skala hejtu, agresji i środowiskowej krytyki, z jaką musiał się zmierzyć Jerzy Brzęczek, zaskakuje, ale i przeraża. Prowokuje do pytania: kim jest jedna z najważniejszych w tej chwili postaci polskiej piłki? Nie tylko jako trener, ale także jako człowiek.\nW grze to mocna, zaskakująca i zmuszająca do refleksji historia jednego z najbardziej „nierozpoznanych” ludzi polskiej piłki. Opowiedziana na wielu poziomach: piłkarskim i prywatnym. Z eliminacjami naszej reprezentacji na EURO 2020 i grozą pandemii koronawirusa w tle. Jest w niej pełnokrwisty bohater, są dramatyczne okoliczności i gwałtowne zwroty akcji. Jest wreszcie sam Jerzy Brzęczek, w którym Małgorzata Domagalik w sposobie rozumienia, pasji i podejściu do piłki nożnej jako takiej widzi w przyszłości kontynuatora trenerskiej myśli Kazimierza Górskiego.\nW książce mówią o selekcjonerze m.in. po raz pierwszy jego żona i synowie, a także trenerzy, dziennikarze, przyjaciele i koledzy z boiska: Kuba Błaszczykowski, Zbigniew Boniek, Hubert Kostka, Andrzej Strejlau, Grzegorz Mielcarski i Krzysztof Materna. ",
                "genre": "sport"
            }
        },
    )


class BookModel(BaseModel):
    """
    Container for a single book record.
    """

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str | list[str] = Field(...)
    author: str | list[str] = Field(...)
    pages: int | list[int] | None = Field(...)
    isbn: str = Field(...)
    publisher: str | list[str] = Field(...)
    original_title: str | list[str] = Field(...)
    release_date: datetime | list[datetime] | None = Field(...)
    release_year: int | list[int] | None = Field(...)
    polish_release_date: datetime | list[datetime] | None = Field(...)
    rating_lc: float | None = Field(...)
    ratings_lc_number: int | None = Field(...)
    rating_tk: float | None = Field(...)
    ratings_tk_number: int | None = Field(...)
    rating_gr: float | None = Field(...)
    ratings_gr_number: int | None = Field(...)
    rating: float | None = Field(...)
    ratings_number: int | None = Field(...)
    img_src: str | list[str] = Field(...)
    description: str | list[str] = Field(...)
    genre: str | list[str] = Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "_id": "65f1dd265dd6e8b74d553390",
                "title": "W grze",
                "author": [
                    "Jerzy Brzęczek",
                    "Malgorzata Domeracka",
                    "Małgorzata Domagalik"
                ],
                "pages": 352,
                "isbn": "9788328075337",
                "publisher": [
                    "W.A.B.",
                    "W.A.B. / GW Foksal"
                ],
                "original_title": "",
                "release_date": [
                    "2020-09-30T20:00:00",
                    "2020-10-21T20:00:00"
                ],
                "release_year": 2020,
                "polish_release_date": "2020-09-30T20:00:00",
                "rating_lc": 3.2,
                "ratings_lc_number": 457,
                "rating_tk": 1,
                "ratings_tk_number": 1,
                "rating_gr": 1.83,
                "ratings_gr_number": 12,
                "rating": 1.6045957446808512,
                "ratings_number": 470,
                "img_src": [
                    "https://bigimg.taniaksiazka.pl/images/popups/5B0/9788328075337.jpg",
                    "https://s.lubimyczytac.pl/upload/books/4941000/4941963/847365-352x500.jpg"
                ],
                "description": " Jego pojawienie się w roli selekcjonera polskiej reprezentacji w 2018 roku wywołało niespotykaną dotąd w naszych mediach burzę. Skala hejtu, agresji i środowiskowej krytyki, z jaką musiał się zmierzyć Jerzy Brzęczek, zaskakuje, ale i przeraża. Prowokuje do pytania: kim jest jedna z najważniejszych w tej chwili postaci polskiej piłki? Nie tylko jako trener, ale także jako człowiek.\nW grze to mocna, zaskakująca i zmuszająca do refleksji historia jednego z najbardziej „nierozpoznanych” ludzi polskiej piłki. Opowiedziana na wielu poziomach: piłkarskim i prywatnym. Z eliminacjami naszej reprezentacji na EURO 2020 i grozą pandemii koronawirusa w tle. Jest w niej pełnokrwisty bohater, są dramatyczne okoliczności i gwałtowne zwroty akcji. Jest wreszcie sam Jerzy Brzęczek, w którym Małgorzata Domagalik w sposobie rozumienia, pasji i podejściu do piłki nożnej jako takiej widzi w przyszłości kontynuatora trenerskiej myśli Kazimierza Górskiego.\nW książce mówią o selekcjonerze m.in. po raz pierwszy jego żona i synowie, a także trenerzy, dziennikarze, przyjaciele i koledzy z boiska: Kuba Błaszczykowski, Zbigniew Boniek, Hubert Kostka, Andrzej Strejlau, Grzegorz Mielcarski i Krzysztof Materna. ",
                "genre": "sport"
            }
        },
    )
