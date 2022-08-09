from datetime import datetime
from typing import Optional

from pydantic import BaseModel, conint, Extra


class DonationCreate(BaseModel):
    full_amount: conint(ge=1)
    comment: Optional[str]

    class Config:
        extra = Extra.forbid


class DonationDB(DonationCreate):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationSuperuserDB(DonationDB):
    user_id: int
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime] = None
