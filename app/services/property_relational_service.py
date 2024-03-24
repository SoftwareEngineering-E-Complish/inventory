from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from app.models.property import Property, Base
from app.schemas.property_query import PropertyQuery

# Specify the database URL
DATABASE_URL = "postgresql://postgres:postgres@postgres-db:5432/postgres"  # Use your actual database URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
print("Table created")

def insert_property(property: Property):
    db = SessionLocal()
    db.add(property)
    db.commit()
    db.refresh(property)
    db.close()

def fetch_property(property_id: int):
    db = SessionLocal()
    statement = select(Property).where(Property.propertyId == property_id)
    property = db.execute(statement).scalars().first()
    db.close()
    return property

def fetch_all():
    db = SessionLocal()
    statement = select(Property)
    properties = db.execute(statement).scalars().all()
    db.close()
    return properties

def fetch_by_attributes(query: PropertyQuery):
    db = SessionLocal()
    statement = set_attributes(query)
    properties = db.execute(statement).scalars().all()
    db.close()
    return properties

def set_attributes(query: PropertyQuery)-> select:
    statement = select(Property)
    if query.price_min:
        statement = statement.where(Property.price >= query.price_min)
    if query.price_max:
        statement = statement.where(Property.price <= query.price_max)
    if query.bedrooms_min:
        statement = statement.where(Property.bedrooms >= query.bedrooms_min)
    if query.bedrooms_max:
        statement = statement.where(Property.bedrooms <= query.bedrooms_max)
    if query.bathroom_min:
        statement = statement.where(Property.bathrooms >= query.bathroom_min)
    if query.bathroom_max:
        statement = statement.where(Property.bathrooms <= query.bathroom_max)
    if query.square_meters_min:
        statement = statement.where(Property.square_meters >= query.square_meters_min)
    if query.square_meters_max:
        statement = statement.where(Property.square_meters <= query.square_meters_max)
    if query.year_built_from:
        statement = statement.where(Property.year_built >= query.year_built_from)
    if query.year_built_to:
        statement = statement.where(Property.year_built <= query.year_built_to)
    if query.property_type:
        statement = statement.where(Property.property_type == query.property_type.value)
    if query.location:
        statement = statement.where(Property.location == query.location.value)
    return statement