from sqlalchemy import Column, String, Integer, UniqueConstraint, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database.db import Base


class Match(Base):
    __tablename__ = "match"

    id = Column(Integer, primary_key=True)
    match = Column(String(50), unique=True)
