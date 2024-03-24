from pydantic import BaseModel, Field
from typing import Any, Dict, Optional
from decimal import Decimal
from enum import Enum

class PropertyType(Enum):
    APARTMENT = "Apartment"
    HOUSE = "House"

class SwissCities(Enum):
    ZURICH = "Zurich"
    GENEVA = "Geneva"
    BASEL = "Basel"
    LAUSANNE = "Lausanne"
    BERN = "Bern"
    LUCERNE = "Lucerne"
    ST_GALLEN = "St. Gallen"
    BIEL = "Biels"
    THUN = "Thun"
    WINTERTHUR = "Winterthur"

class Property(BaseModel):
    propertyId: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None 
    location: Optional[SwissCities] = None
    bedrooms: Optional[int] = Field(None, ge=1, le=10, description="Number of bedrooms in the property")
    bathrooms: Optional[int] = None
    square_meters: Optional[int] = None
    year_built: Optional[int] = None
    property_type: Optional[PropertyType] = Field(None, description="Type of the property")

    done: Optional[bool] = None

    # Convert the Property object to a dictionary ensuring that the Enum values are converted to their string representation
    # This is needed to ensure that the Enum values are serialized correctly for DynamoDB
    def model_dump(self) -> Dict[str, Any]:
        return {k: (v.value if isinstance(v, Enum) else v) for k, v in super().model_dump().items()}