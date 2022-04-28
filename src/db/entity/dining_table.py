from data import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, String, Boolean, func


class DiningTable(Base):
    __tablename__ = "DiningTable"

    id = Column(Integer, primary_key=True, autoincrement=True)
    table_no = Column(String(40), nullable=False)
    description = Column(String(60), nullable=False)
    restaurant_id = Column(Integer, ForeignKey("Restaurant.id", ondelete="CASCADE"))
    occupied = Column(Boolean, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    modified_at = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    created_by = Column(String(50), nullable=False)
    modified_by = Column(String(50), nullable=True)