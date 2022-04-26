from data import Base
from sqlalchemy import Column, Integer, ForeignKey


class DishTag(Base):
    __tablename__ = "DishTag"

    id = Column(Integer, primary_key=True, autoincrement=True)
    dish_id = Column(Integer, ForeignKey("Dish.id"), nullable=False)
    tag_id = Column(Integer, ForeignKey("Tag.id"), nullable=False)