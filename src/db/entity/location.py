from data import Base
from db.enums.enum import TagType
from sqlalchemy import Column, String, Enum, Integer, DateTime, func


class Location(Base):
    __tablename__ = "Location"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False)
    created_by = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    modified_by = Column(String(50), nullable=True)
    modified_at = Column(DateTime(timezone=True), nullable=True,  server_onupdate=func.now())
