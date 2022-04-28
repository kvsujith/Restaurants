from data import Base
from db.enums.enum import OrderType, OrderStatus
from sqlalchemy import Column, String, Integer, DateTime, Enum, ForeignKey, func


class Order(Base):

    __tablename__ = "Order"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_type = Column(Enum(OrderType))
    dining_table_id = Column(Integer, ForeignKey("DiningTable.id", ondelete="CASCADE"), nullable=False)
    special_message = Column(String(40))
    status = Column(Enum(OrderStatus))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    modified_at = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    created_by = Column(String(50), nullable=False)
    modified_by = Column(String(50), nullable=True)
