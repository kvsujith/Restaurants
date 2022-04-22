from data import Base
from src.utils.utils import get_indian_time
from sqlalchemy import Column, Integer, ForeignKey, DateTime, String, Boolean


class DiningTable(Base):
    __tablename__ = "DiningTable"

    id = Column(Integer, primary_key=True, autoincrement=True)
    table_no = Column(String(40), nullable=False)
    description = Column(String(60), nullable=False)
    restaurant_id = Column(Integer, ForeignKey("Restaurant.id"))
    occupied = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=get_indian_time())
    modified_at = Column(DateTime, onupdate=get_indian_time())
    created_by = Column(String(50), nullable=False)
    modified_by = Column(String(50), nullable=False)