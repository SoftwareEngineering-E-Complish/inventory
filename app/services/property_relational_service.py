from sqlalchemy import create_engine, select, func, Select, Sequence
from sqlalchemy.orm import sessionmaker
from app.models.property import Property, Base
from app.schemas.property_query import PropertyQuery, ResultOrder
from typing import Tuple
from os import getenv

# Specify the database URL
DATABASE_URL = getenv("DATABASE_URL")

engine = create_engine(str(DATABASE_URL))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Base.metadata.create_all(bind=engine)


def insert_property(property: Property)-> Property:
    #set key to null even if it is provided so it can be autogenerated
    property.propertyId = None #type: ignore
    db = SessionLocal()
    db.add(property)
    db.commit()
    db.refresh(property)
    db.close()
    return property

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

def fetch_by_attributes(query: PropertyQuery)-> Tuple[Sequence[Property], int]:
    db = SessionLocal()
    count_statement = select(func.count()).select_from(Property)
    count_statement = set_attributes(query, count_statement)
    count = db.execute(count_statement).scalar()
    statement = select(Property)
    statement = set_attributes(query, statement)
    statement = set_pagination(query, statement)
    statement = set_order(query, statement)
    properties = db.execute(statement).scalars().all()
    db.close()
    return properties, count #type: ignore

def set_attributes(query: PropertyQuery,  statement: Select)-> Select:
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

def set_pagination(query: PropertyQuery, statement: Select)-> Select:
    if query.limit:
        statement = statement.limit(query.limit)
    if query.offset:
        statement = statement.offset(query.offset)
    return statement

def set_order(query: PropertyQuery, statement: Select) -> Select:
    if query.order:
        if query.order == ResultOrder.PRICE_ASC:
            statement = statement.order_by(Property.price)
        elif query.order == ResultOrder.PRICE_DESC:
            statement = statement.order_by(Property.price.desc())
        elif query.order == ResultOrder.BEDROOMS_ASC:
            statement = statement.order_by(Property.bedrooms)
        elif query.order == ResultOrder.BEDROOMS_DESC:
            statement = statement.order_by(Property.bedrooms.desc())
        elif query.order == ResultOrder.BATHROOMS_ASC:
            statement = statement.order_by(Property.bathrooms)
        elif query.order == ResultOrder.BATHROOMS_DESC:
            statement = statement.order_by(Property.bathrooms.desc())
        elif query.order == ResultOrder.SQUARE_METERS_ASC:
            statement = statement.order_by(Property.square_meters)
        elif query.order == ResultOrder.SQUARE_METERS_DESC:
            statement = statement.order_by(Property.square_meters.desc())
        elif query.order == ResultOrder.YEAR_BUILT_ASC:
            statement = statement.order_by(Property.year_built)
        elif query.order == ResultOrder.YEAR_BUILT_DESC:
            statement = statement.order_by(Property.year_built.desc())
    return statement