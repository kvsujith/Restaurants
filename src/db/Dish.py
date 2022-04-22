from .BaseDB import Base
from .Utils import get_indian_time
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean


class Dish(Base):
    __tablename__ = "Dish"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False)
    description = Column(String(60), nullable=False)
    restaurant_id = Column(Integer, ForeignKey("Restaurant.id"))
    availability = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=get_indian_time())
    modified_at = Column(DateTime, onupdate=get_indian_time())
    created_by = Column(String(50), nullable=False)
    modified_by = Column(String(50), nullable=False)