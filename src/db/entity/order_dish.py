from data import Base
from sqlalchemy import Column, Integer, ForeignKey


class OrderDish(Base):

    __tablename__ = "OrderDish"

    id = Column(Integer, primary_key=True, autoincrement=True)
    dish_id = Column(Integer, ForeignKey("Dish.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("Order.id"), nullable=False)

