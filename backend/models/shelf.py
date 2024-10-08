from pydantic import ConfigDict, BaseModel, Field
from typing import Optional
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]


class ShelfModel(BaseModel):
    """
    Container for a single shelf record.
    """

    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    user_id: Optional[PyObjectId] = Field(alias="_id", default=None)
    books: list[str] | None = Field(...)
    is_default: bool = Field(...)

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "_id": "6604317bf130179fad967189",
                "name": "Przeczytane",
                "books": ["9788367133210", "9788379984817"],
                "is_default": True,
            }
        },
    )
