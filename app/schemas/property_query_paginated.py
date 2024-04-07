from pydantic import BaseModel, Field
from typing import Optional, List
from app.schemas.property import Property

class PropertyListPaginated(BaseModel):
    entries: List[Property] = Field([], description="List of query results")
    total: int = Field(0, description="Total number of entries")
    offset: int = Field(0, description="Offset to start the entries from")
    limit: int = Field(10, description="Number of entries to return per page")