from pydantic import BaseModel, Field
from typing import Optional, List
from .property import PropertyType, SwissCities
from enum import Enum

class ResultOrder(Enum):
    PRICE_ASC = "price-asc"
    PRICE_DESC = "price-desc"
    BEDROOMS_ASC = "bedrooms-asc"
    BEDROOMS_DESC = "bedrooms-desc"
    BATHROOMS_ASC = "bathrooms-asc"
    BATHROOMS_DESC = "bathrooms-desc"
    SQUARE_METERS_ASC = "square-meters-asc"
    SQUARE_METERS_DESC = "square-meters-desc"
    YEAR_BUILT_ASC = "year-built-asc"
    YEAR_BUILT_DESC = "year-built-desc"

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
    limit: Optional[int] = Field(10, description="Number of entries to return per page")
    offset: Optional[int] = Field(0, description="Offset to start the entries from")
    order: Optional[ResultOrder] = Field(None, description="Order to sort the results by")


class QueryBasic(BaseModel):
    sample_int: int = Field(None, description="Sample int")
    sample_str: str = Field(None, description="Sample string")
    sample_bool: bool 
    sample_enum: PropertyType
    sample_list: List[str]
