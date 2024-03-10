from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class Property(BaseModel):
    propertyId: str = 0
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None 
    location: Optional[str] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    square_meters: Optional[int] = None
    year_built: Optional[int] = None
    property_type: Optional[str] = None
    done: Optional[bool] = None