from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Float,
    DateTime,
    UniqueConstraint,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ...database.db import Base


class Asin(Base):
    __tablename__ = "bid_asin"
    __table_args__ = (
        UniqueConstraint("asin", "sku", "sales_channel_id", name="uix_ass"),
    )

    asin_id = Column(Integer, primary_key=True)
    asin = Column(String(10), nullable=False)
    sku = Column(String(25), nullable=False)
    sales_channel_id = Column(Integer, nullable=False)
    market = Column(String(10), nullable=False)
    list_price = Column(
        Float,
    )
    procurement_status = Column(String(50))
    sem_status = Column(String(50))
    compliment_bid_profile_id = Column(
        ForeignKey("bid_profile.bid_profile_id"), nullable=True, default=1
    )
    close_bid_profile_id = Column(
        ForeignKey("bid_profile.bid_profile_id"), nullable=True, default=1
    )
    loose_bid_profile_id = Column(
        ForeignKey("bid_profile.bid_profile_id"), nullable=True, default=1
    )
    substitute_bid_profile_id = Column(
        ForeignKey("bid_profile.bid_profile_id"), nullable=True, default=1
    )
    broad_bid_profile_id = Column(
        ForeignKey("bid_profile.bid_profile_id"), nullable=True, default=1
    )
    exact_bid_profile_id = Column(
        ForeignKey("bid_profile.bid_profile_id"), nullable=True, default=1
    )
    phrase_bid_profile_id = Column(
        ForeignKey("bid_profile.bid_profile_id"), nullable=True, default=1
    )
    created_datetime = Column(DateTime(timezone=True), server_default=func.now())
    updated_datetime = Column(DateTime(timezone=True), onupdate=func.now())

    bid_profile = relationship("BidProfile")
