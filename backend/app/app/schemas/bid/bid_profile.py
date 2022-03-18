from pydantic import BaseModel
from typing import Optional
import datetime as dt


class BidProfileBase(BaseModel):
    name: Optional[str] = None
    note: Optional[str] = None
    target_acos: Optional[float] = None
    min_target_acos_boundary: Optional[float] = None
    max_target_acos_boundary: Optional[float] = None
    max_acos: Optional[float] = None
    min_clicks: Optional[int] = None
    min_impressions: Optional[int] = None
    floor_bid: Optional[float] = None
    ceiling_bid: Optional[float] = None
    increment_up_rate: Optional[float] = None
    increment_down_rate: Optional[float] = None
    max_increment_up: Optional[float] = None
    max_increment_down: Optional[float] = None


class BidProfileCreate(BidProfileBase):
    name: str
    target_acos: float
    min_target_acos_boundary: float
    max_target_acos_boundary: float
    max_acos: float
    min_clicks: int
    min_impressions: int
    floor_bid: float
    ceiling_bid: float
    increment_up_rate: float
    increment_down_rate: float


class BidProfileUpdate(BidProfileBase):
    pass


class BidProfileInDBBase(BaseModel):
    bid_profile_id: Optional[int]
    name: Optional[str] = None
    note: Optional[str] = None
    target_acos: Optional[float] = None
    min_target_acos_boundary: Optional[float] = None
    max_target_acos_boundary: Optional[float] = None
    max_acos: Optional[float] = None
    min_clicks: Optional[int] = None
    min_impressions: Optional[int] = None
    floor_bid: Optional[float] = None
    ceiling_bid: Optional[float] = None
    increment_up_rate: Optional[float] = None
    increment_down_rate: Optional[float] = None
    max_increment_up: Optional[float] = None
    max_increment_down: Optional[float] = None
    created_datetime: Optional[dt.datetime] = None
    updated_datetime: Optional[dt.datetime] = None

    class Config:
        orm_mode = True


class BidProfile(BidProfileInDBBase):
    pass
