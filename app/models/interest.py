from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.models.base import Base

class Interest(Base):
    __tablename__ = 'interest'

    propertyId = Column(Integer, ForeignKey('property.propertyId'), primary_key=True)
    userId = Column(String, primary_key=True)
    timestamp = Column(DateTime)