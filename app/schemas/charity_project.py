from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, conint, validator


class CharityProjectCreate(BaseModel):
    name: str = Field(max_length=100)
    description: str
    full_amount: conint(ge=1)

    class Config:
        min_anystr_length = 1
        extra = Extra.forbid


class CharityProjectUpdate(CharityProjectCreate):
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str]
    full_amount: Optional[conint(ge=1)]

    @validator('name', 'full_amount', 'description')
    def check_fields_is_none(cls, value):
        print(value)
        if not value:
            raise ValueError(
                'Название и описание проекта не должны быть пустыми'
            )
        return value


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime] = None

    class Config:
        orm_mode = True
