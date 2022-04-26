from data import Base
from src.utils.utils import get_indian_time
from sqlalchemy import Column, String, Integer, DateTime


class Restaurant(Base):
    __tablename__ = "Restaurant"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False)
    description = Column(String(60), nullable=False)
    created_at = Column(DateTime, default=get_indian_time(), nullable=False)
    modified_at = Column(DateTime, onupdate=get_indian_time(), nullable=True)
    created_by = Column(String(50), nullable=False)
    modified_by = Column(String(50), nullable=True)
