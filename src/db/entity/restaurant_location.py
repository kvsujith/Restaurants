from data import Base
from sqlalchemy import Column, Integer, ForeignKey


class RestaurantLocation(Base):
    __tablename__ = "RestaurantLocation"

    id = Column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = Column(Integer, ForeignKey("Restaurant.id"))
    location_id = Column(Integer, ForeignKey("Location.id"))