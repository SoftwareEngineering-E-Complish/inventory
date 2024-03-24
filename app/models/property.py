from sqlalchemy import Column, Integer, String, Numeric, Enum, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Property(Base):
    __tablename__ = 'property'

    propertyId = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    price = Column(Numeric)
    location = Column(String)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    square_meters = Column(Integer)
    year_built = Column(Integer)
    property_type = Column(String)
    done = Column(Boolean)