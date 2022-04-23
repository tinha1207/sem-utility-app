from sqlalchemy import (
    Column,
    ForeignKey,
    UniqueConstraint,
    String,
    Integer,
    Boolean,
    DateTime,
    Float,
    text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database.db import Base


class BidTarget(Base):
    __tablename__ = "bid_target"
    __table_args__ = (UniqueConstraint("asin_id", "match_id", name="uix_bid_target"),)

    id = Column(Integer, primary_key=True)
    asin_id = Column(Integer, ForeignKey("asin.id", ondelete="CASCADE"), nullable=False)
    match_id = Column(Integer, ForeignKey("match.id"), nullable=False)
    min_impressions = Column(Integer)
    lower_acos_target_boundary = Column(Float, nullable=False)
    upper_acos_target_boundary = Column(Float, nullable=False)
    max_acos = Column(Float, nullable=False)
    min_clicks = Column(Integer)
    bid_increment = Column(Float, nullable=False)
    bid_decrement = Column(Float, nullable=False)
    min_bid = Column(Float, nullable=False)
    max_bid = Column(Float, nullable=False)
    is_enabled = Column(Boolean, server_default="1")
    created_datetime = Column(DateTime(timezone=True), server_default=func.now())
    updated_datetime = Column(
        DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )

    asin = relationship("Asin", back_populates="bid_targets")
    match = relationship("Match")
