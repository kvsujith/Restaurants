from data import Base
from db.enums.enum import OrderType, OrderStatus
from src.utils.utils import get_indian_time
from sqlalchemy import Column, String, Integer, DateTime, Enum, ForeignKey


class Order(Base):

    __tablename__ = "Order"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_type = Column(Enum(OrderType))
    dining_table_id = Column(Integer, ForeignKey("DiningTable.id"), nullable=False)
    special_message = Column(String(40))
    status = Column(Enum(OrderStatus))
    created_at = Column(DateTime, default=get_indian_time())
    modified_at = Column(DateTime, onupdate=get_indian_time())
    created_by = Column(String(50), nullable=False)
    modified_by = Column(String(50), nullable=False)
