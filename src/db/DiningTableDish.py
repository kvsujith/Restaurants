from .BaseDB import Base
from sqlalchemy import Column, Integer, ForeignKey


class DiningTableDish(Base):
    __tablename__ = "DiningTableDish"

    id = Column(Integer, primary_key=True, autoincrement=True)
    dish_id = Column(Integer, ForeignKey("Dish.id"), nullable=False)
    dining_table_id = Column(Integer, ForeignKey("DiningTable.id"), nullable=False)
