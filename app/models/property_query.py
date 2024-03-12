import json, jsonref
from pydantic import BaseModel, Field
from typing import Optional, List, Any
from .property import PropertyType, SwissCities

class PropertyQuery(BaseModel):
    price_min: Optional[int] = Field(None, description="Minimum price of the property")
    price_max: Optional[int] = Field(None, description="Maximum price of the property")
    bedrooms_min: Optional[int] = Field(None, ge=1, description="Minimum number of bedrooms in the property. Must be at least 1.")
    bedrooms_max: Optional[int] = Field(None, le=10, description="Maximum number of bedrooms in the property. Must be at most 10.")
    bathroom_min: Optional[int] = Field(None, description="Minimum number of bathrooms in the property")
    bathroom_max: Optional[int] = Field(None, description="Maximum number of bathrooms in the property")
    square_meters_min: Optional[int] = Field(None, description="Minimum square meters of the property")
    square_meters_max: Optional[int] = Field(None, description="Maximum square meters of the property")
    year_built_from: Optional[int] = Field(None, description="Minimum year the property was built")
    year_built_to: Optional[int] = Field(None, description="Maximum year the property was built")
    property_type: Optional[PropertyType] = Field(None, description="Type of the property")
    location: Optional[SwissCities] = Field(None, description="Location of the property, only specific Swiss cities are allowed")

"""
class Parameter:
    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        self.description = description
"""

class QueryBasic(BaseModel):
    sample_int: int = Field(None, description="Sample int")
    sample_str: str = Field(None, description="Sample string")
    sample_bool: bool 
    sample_enum: PropertyType
    sample_list: List[str]


"""
class QueryBasic(BaseModel):
    price_min: int = Field(description="Minimum price of the property")
    price_max: int = Field(description="Maximum price of the property")
    bedrooms_min: int = Field(ge=1, description="Minimum number of bedrooms in the property. Must be at least 1.")
    bedrooms_max: int = Field(le=10, description="Maximum number of bedrooms in the property. Must be at most 10.")
    bathroom_min: int = Field(description="Minimum number of bathrooms in the property")
    bathroom_max: int = Field(description="Maximum number of bathrooms in the property")
    square_meters_min: int = Field(description="Minimum square meters of the property")
    square_meters_max: int = Field(description="Maximum square meters of the property")
    year_built_from: int = Field(description="Minimum year the property was built")
    year_built_to: int = Field(description="Maximum year the property was built")
    property_type: PropertyType = Field(description="Type of the property") """