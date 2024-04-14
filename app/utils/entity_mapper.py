from app.models.property import Property as PropertyModel
from app.schemas.property import Property as PropertySchema
from geoalchemy2 import WKTElement
from geoalchemy2.shape import to_shape
from shapely.errors import GEOSException

def schemaToModel(schema: PropertySchema) -> PropertyModel:
    modelProperty = PropertyModel()
    modelProperty.propertyId = schema.propertyId
    modelProperty.title = schema.title
    modelProperty.description = schema.description
    modelProperty.price = schema.price
    if schema.location:
        modelProperty.location = schema.location.value
    modelProperty.bedrooms = schema.bedrooms
    modelProperty.bathrooms = schema.bathrooms
    modelProperty.square_meters = schema.square_meters
    modelProperty.year_built = schema.year_built
    if schema.property_type:
        modelProperty.property_type = schema.property_type.value
    modelProperty.done = schema.done
    modelProperty.owner = schema.owner
    if schema.latitude and schema.longitude:
        modelProperty.location_pin = WKTElement(f"POINT({schema.longitude} {schema.latitude})", srid=4326)
    return modelProperty

def modelToSchema(model: PropertyModel) -> PropertySchema:
    schemaProperty = PropertySchema(**model.__dict__)
    try:
        point = to_shape(model.location_pin) #type: ignore
        schemaProperty.longitude = point.x
        schemaProperty.latitude = point.y
    except (GEOSException, AssertionError):
        schemaProperty.longitude = None
        schemaProperty.latitude = None
    
    return schemaProperty