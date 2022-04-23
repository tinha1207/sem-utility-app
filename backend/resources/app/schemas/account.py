from pydantic import BaseModel, constr
from typing import Optional


class AccountBase(BaseModel):
    name: Optional[str]
    account: Optional[str]
    platform: Optional[str]
    sales_channel_id: Optional[int]
    country_code: Optional[str]
    prefix: Optional[str]


class AccountCreate(AccountBase):
    name: str
    account: str
    platform: str
    sales_channel_id: int
    country_code: constr(max_length=2, min_length=2, strip_whitespace=True)
    prefix: str


class AccountUpdate(AccountBase):
    pass


class AccountBaseDB(BaseModel):
    id: int
    name: Optional[str]
    account: Optional[str]
    platform: Optional[str]
    sales_channel_id: Optional[int]
    country_code: Optional[str]
    campaign_prefix: Optional[str]

    class Config:
        orm_mode = True


class Account(AccountBaseDB):
    pass
