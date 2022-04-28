from data import Base
from db.enums.enum import OrderStatus
from sqlalchemy import Column, Integer, ForeignKey, Enum, DateTime, String, func


class Invoice(Base):

    __tablename__ = "Invoice"

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(Enum(OrderStatus), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    modified_at = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    created_by = Column(String(50), nullable=False)
    modified_by = Column(String(50), nullable=True)

    restaurant_id = Column(Integer, ForeignKey("Restaurant.id", ondelete="CASCADE"), nullable=False)
    order_id = Column(Integer, ForeignKey("Order.id", ondelete="CASCADE"), nullable=False)
