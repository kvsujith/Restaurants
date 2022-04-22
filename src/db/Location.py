from .BaseDB import Base
from .Utils import get_indian_time
from .ENUMS.TagType import TagType
from sqlalchemy import Column, String, Enum, Integer, DateTime


class Location(Base):
    __tablename__ = "Location"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False)
    type = Column(Enum(TagType))
    created_at = Column(DateTime, default=get_indian_time())
    modified_at = Column(DateTime, onupdate=get_indian_time())
    created_by = Column(String(50), nullable=False)
    modified_by = Column(String(50), nullable=False)
