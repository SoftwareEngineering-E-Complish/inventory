from app.models.property import Property as PropertyModel
from app.schemas.property import Property as PropertySchema
from geoalchemy2 import WKTElement
from geoalchemy2.shape import to_shape
from shapely.errors import GEOSException

def schemaToModel(schema: PropertySchema) -> PropertyModel:
    modelProperty = PropertyModel()
    modelProperty.propertyId = schema.propertyId #type: ignore
    modelProperty.title = schema.title #type: ignore
    modelProperty.description = schema.description #type: ignore
    modelProperty.price = schema.price #type: ignore
    if schema.location:
        modelProperty.location = schema.location.value #type: ignore
    modelProperty.bedrooms = schema.bedrooms #type: ignore
    modelProperty.bathrooms = schema.bathrooms #type: ignore
    modelProperty.square_meters = schema.square_meters #type: ignore
    modelProperty.year_built = schema.year_built #type: ignore
    if schema.property_type:
        modelProperty.property_type = schema.property_type.value #type: ignore
    modelProperty.done = schema.done #type: ignore
    modelProperty.owner = schema.owner #type: ignore
    modelProperty.address = schema.address #type: ignore
    if schema.latitude and schema.longitude:
        modelProperty.location_pin = WKTElement(f"POINT({schema.longitude} {schema.latitude})", srid=4326) #type: ignore
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