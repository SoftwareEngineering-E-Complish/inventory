#import debugpy
#debugpy.listen(("0.0.0.0", 5678))
from app.services.property_service import create_property_autoKey, get_all_properties, get_property, query_properties_by_attributes
from app.schemas.property import Property
from app.schemas.property_query import PropertyQuery
from app.schemas.property_query_paginated import PropertyQueryPaginated
from app.services.property_relational_service import insert_property, fetch_property, fetch_all, fetch_by_attributes
from app.utils.entity_mapper import schemaToModel, modelToSchema
from typing import List
from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()

@app.get("/schema/propertyQuery")
def get_schema():
    return PropertyQuery.model_json_schema(by_alias=True)

@app.get("/properties/", response_model=List[Property])
def fetch_all_properties():
    propertiesModel = fetch_all()
    properties = []
    for propertyModel in propertiesModel:
        properties.append(modelToSchema(propertyModel))
    return properties

@app.get("/propetries/{property_id}", response_model=Property)
def fetch_property_by_key(property_id: str):
    id = int(property_id)
    item = fetch_property(id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.get("/queryProperties", response_model=PropertyQueryPaginated, description="Query the properties based on the fields provided")
def query_properties(query: PropertyQuery = Depends(PropertyQuery)):
    propertiesModel, countAll = fetch_by_attributes(query)
    properties = []
    for propertyModel in propertiesModel:
        properties.append(modelToSchema(propertyModel))
    return PropertyQueryPaginated(entries=properties, total=countAll, offset=query.offset, limit=query.limit)

@app.post("/properties/", response_model=Property)
def create_property_listing(property: Property):
    insert_property(schemaToModel(property))
    return property

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



