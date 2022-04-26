from data import Base
from src.utils.utils import get_indian_time
from sqlalchemy import Column, Integer , DateTime, String


class Customer(Base):
    __tablename__ = "Customer"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(10), nullable=False, unique=True)
    created_at = Column(DateTime, default=get_indian_time())
    modified_at = Column(DateTime, onupdate=get_indian_time())
    created_by = Column(String(50), nullable=False)
    modified_by = Column(String(50), nullable=False)
