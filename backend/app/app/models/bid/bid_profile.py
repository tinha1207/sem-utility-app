from sqlalchemy import Column, String, Float, Integer, DateTime, null
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ...database.db import Base


class BidProfile(Base):
    __tablename__ = "bid_profile"

    bid_profile_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    note = Column(String(255), default=null)
    target_acos = Column(Float, default=0.2, nullable=False)
    min_target_acos_boundary = Column(Float, nullable=False)
    max_target_acos_boundary = Column(Float, nullable=False)
    max_acos = Column(Float, nullable=False)
    min_clicks = Column(Integer, nullable=False)
    min_impressions = Column(Integer, nullable=False)
    floor_bid = Column(Float, nullable=False)
    ceiling_bid = Column(Float, nullable=False)
    increment_up_rate = Column(Float, nullable=False)
    increment_down_rate = Column(Float, nullable=False)
    max_increment_up = Column(Float)
    max_increment_down = Column(Float)
    created_datetime = Column(DateTime(timezone=True), server_default=func.now())
    updated_datetime = Column(DateTime(timezone=True), onupdate=func.now())
