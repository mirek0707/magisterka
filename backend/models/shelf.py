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

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={"example": {}},
    )
