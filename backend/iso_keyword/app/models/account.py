from sqlalchemy import Column, String, Integer, UniqueConstraint

from app.database.db import Base

class Account(Base):
    __tablename__= "account"
    __table_args__= (
        UniqueConstraint("account", "platform", "sales_channel_id", "country_code", name="uix_prefix"),
    )

    id = Column(Integer, primary_key=True)
    account = Column(String(100),nullable=False)
    platform = Column(String(100), nullable=False)
    sales_channel_id = Column(Integer, nullable=False)
    country_code = Column(String(2),nullable=False)
    prefix = Column(String(100),nullable =False)