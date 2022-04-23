from sqlalchemy import Column, String, Integer, UniqueConstraint, text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database.db import Base


class Account(Base):
    __tablename__ = "account"
    __table_args__ = (
        UniqueConstraint(
            "account",
            "platform",
            "sales_channel_id",
            "country_code",
            name="uix_account",
        ),
    )

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, index=True)
    account = Column(String(100), nullable=False)
    platform = Column(String(100), nullable=False)
    sales_channel_id = Column(Integer, nullable=False)
    country_code = Column(String(2), nullable=False)
    campaign_prefix = Column(String(100), nullable=False)
    created_datetime = Column(DateTime(timezone=True), server_default=func.now())
    updated_datetime = Column(
        DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )
