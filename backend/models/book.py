from pydantic import ConfigDict, BaseModel, Field
from typing import Optional
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator
from datetime import datetime

PyObjectId = Annotated[str, BeforeValidator(str)]


class BookModel(BaseModel):
    """
    Container for a single book record.
    """

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str | list = Field(...)
    author: str | list = Field(...)
    pages: int | list | None = Field(...)
    isbn: str = Field(...)
    publisher: str | list = Field(...)
    original_title: str | list = Field(...)
    release_date: datetime | list | None = Field(...)
    release_year: int | list | None = Field(...)
    polish_release_date: datetime | list | None = Field(...)
    rating_lc: float | None = Field(...)
    ratings_lc_number: int | None = Field(...)
    rating_tk: float | None = Field(...)
    ratings_tk_number: int | None = Field(...)
    rating_gr: float | None = Field(...)
    ratings_gr_number: int | None = Field(...)
    rating: float = Field(...)
    ratings_number: int = Field(...)
    img_src: str | list = Field(...)
    description: str | list = Field(...)
    genre: str | list = Field(...)

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
