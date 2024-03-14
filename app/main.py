#import debugpy
#debugpy.listen(("0.0.0.0", 5678))
from app.services.property_service import create_property_autoKey, get_all_properties, get_property, query_properties_by_attributes
from app.models.property import Property
from app.models.property_query import PropertyQuery
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi import HTTPException, Depends

app = FastAPI()

@app.get("/schema/propertyQuery")
def get_schema():
    return PropertyQuery.model_json_schema(by_alias=True)

@app.get("/properties/", response_model=List[Property])
def fetch_all_properties():
    return get_all_properties()

@app.get("/propetries/{property_id}", response_model=Property)
def fetch_property_by_key(property_id: str):
    item = get_property(property_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.get("/queryProperties", response_model=List[Property], description="Query the properties based on the fields provided")
def query_properties(query: PropertyQuery = Depends(PropertyQuery)):
    return query_properties_by_attributes(query)

@app.post("/properties/", response_model=Property)
def create_property_listing(property: Property):
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



