from .BaseDB import Base
from .Utils import get_indian_time
from .ENUMS.OrderStatus import OrderStatus
from sqlalchemy import Column, Integer, ForeignKey, Enum, DateTime, String


class Invoice(Base):
    __tablename__ = "Invoice"

    id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = Column(Integer, ForeignKey("Restaurant.id"))
    order_id = Column(Integer, ForeignKey("Order.id"))
    status = Column(Enum(OrderStatus), nullable=False)
    created_at = Column(DateTime, default=get_indian_time())
    modified_at = Column(DateTime, onupdate=get_indian_time())
    created_by = Column(String(50), nullable=False)
    modified_by = Column(String(50), nullable=False)
