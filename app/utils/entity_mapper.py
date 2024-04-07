from app.models.property import Property as PropertyModel
from app.schemas.property import Property as PropertySchema

def schemaToModel(schema: PropertySchema) -> PropertyModel:
    return PropertyModel(**schema.model_dump())

def modelToSchema(model: PropertyModel) -> PropertySchema:
    return PropertySchema(**model.__dict__)