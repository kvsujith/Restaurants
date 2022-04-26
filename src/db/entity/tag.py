from data import Base
from db.enums.enum import TagType
from sqlalchemy import Column, String, Enum, Integer, DateTime, func


class Tag(Base):

    __tablename__ = "Tag"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False)
    type = Column(Enum(TagType), default=TagType(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    modified_at = Column(DateTime(timezone=True), nullable=True,  server_onupdate=func.now())
    created_by = Column(String(50), nullable=False)
    modified_by = Column(String(50), nullable=True)

    def __repr__(self):
        return f"{self.id} {self.name} {self.type}"
