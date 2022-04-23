from faulthandler import is_enabled
from sqlalchemy import (
    Column,
    Float,
    ForeignKey,
    UniqueConstraint,
    String,
    Integer,
    Boolean,
    DateTime,
    null,
    text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database.db import Base


class Asin(Base):
    __tablename__ = "asin"
    __table_args__ = (UniqueConstraint("asin", "sku", "account_id", name="uix_asin"),)

    id = Column(Integer, primary_key=True)
    asin = Column(String(10), index=True, nullable=False)
    sku = Column(String(50), index=True, nullable=False)
    account_id = Column(
        Integer,
        ForeignKey("account.id", ondelete="SET NULL"),
    )
    initiative = Column(String(100), default=null)
    target_acos = Column(Float, nullable=False)
    is_enabled = Column(Boolean, server_default="1")
    is_iso = Column(Boolean, server_default="0")
    created_datetime = Column(DateTime(timezone=True), server_default=func.now())
    updated_datetime = Column(
        DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )

    account = relationship("Account", back_populates="asins")
    bid_targets = relationship("BidTarget", back_populates="asin")
