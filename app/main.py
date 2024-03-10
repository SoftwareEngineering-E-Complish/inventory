#import debugpy
#debugpy.listen(("0.0.0.0", 5678))
from app.services.property_service import create_property_autoKey, get_all_properties, get_property, get_properties_by_attributes
from app.models.property import Property
from typing import List
from fastapi import FastAPI, HTTPException
from typing import Optional
from fastapi import HTTPException, Depends
from decimal import Decimal 

app = FastAPI()

@app.get("/properties/", response_model=List[Property])
def fetch_all_properties():
    return get_all_properties()

@app.get("/propetries/{property_id}", response_model=Property)
def fetch_property_by_key(property_id: str):
    item = get_property(property_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

def query_params_to_property(title: Optional[str] = None,
                             description: Optional[str] = None,
                             price: Optional[Decimal] = None,
                             location: Optional[str] = None,
                             bedrooms: Optional[int] = None,
                             bathrooms: Optional[int] = None,
                             square_meters: Optional[int] = None,
                             year_built: Optional[int] = None,
                             property_type: Optional[str] = None,
                             done: Optional[bool] = None) -> Property:
    return Property(title=title,
                    description=description,
                    price=price,
                    location=location,
                    bedrooms=bedrooms,
                    bathrooms=bathrooms,
                    square_meters=square_meters,
                    year_built=year_built,
                    property_type=property_type,
                    done=done)

@app.get("/queryPropertiesByAttributes", response_model=List[Property], description="Fetch all the Properties matching the fields provided as parameters")
def fetch_properties_by_attrivutes(exampleProperty: Property = Depends(query_params_to_property)):
    #return [exampleProperty]
    return get_properties_by_attributes(exampleProperty)

@app.post("/properties/", response_model=Property)
def create_prop(property: Property):
    created_item = create_property_autoKey(property)
    return created_item

"""
@app.put("/items/{item_id}", response_model=Property)
def update_todo_item(item_id: str, updates: Property):
    item = update_item(item_id, updates.model_dump())
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item"""

"""
@app.delete("/items/{item_id}", response_model=dict)
def delete_todo_item(item_id: str):
    response = delete_item(item_id)
    if 'ResponseMetadata' not in response:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"} """



