from data import Base
from db.enums.enum import OrderStatus
from src.utils.utils import get_indian_time

from sqlalchemy import Column, Integer, ForeignKey, Enum, DateTime, String


class Invoice(Base):

    __tablename__ = "Invoice"

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(Enum(OrderStatus), nullable=False)
    created_at = Column(DateTime, default=get_indian_time())
    modified_at = Column(DateTime, onupdate=get_indian_time())
    created_by = Column(String(50), nullable=False)
    modified_by = Column(String(50), nullable=False)

    restaurant_id = Column(Integer, ForeignKey("Restaurant.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("Order.id"), nullable=False)
