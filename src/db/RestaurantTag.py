from .BaseDB import Base
from .Utils import get_indian_time
from sqlalchemy import Column, Integer, ForeignKey


class RestaurantTag(Base):
    __tablename__ = "RestaurantTag"

    id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = Column(Integer, ForeignKey("Restaurant.id"))
    tag_id = Column(Integer, ForeignKey("Tag.id"))
