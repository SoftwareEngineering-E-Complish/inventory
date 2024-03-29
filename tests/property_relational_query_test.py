import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from sqlalchemy import Select
from app.models.property import Property
from app.schemas.property_query import PropertyQuery , ResultOrder
from app.schemas.property import PropertyType, SwissCities
from app.services.property_relational_service import set_attributes, set_pagination, set_order

# This test case is to test the condition expression for the scan operation
class TestPropertyQuery(unittest.TestCase):
    
    def test_condition_empty(self):
        query = PropertyQuery() # type: ignore
        conditions = set_attributes(query, Select(Property))
        self.assertEqual(str(conditions), str(Select(Property)))

    def test_condition_price_min(self):
        query = PropertyQuery(price_min=100000) # type: ignore
        conditions = set_attributes(query, Select(Property))
        expectedValue = Select(Property).where(Property.price >= 100000)
        self.assertEqual(str(conditions), str(expectedValue))
    
    def test_condition_price_max(self):
        query = PropertyQuery(price_max=100000) # type: ignore
        conditions = set_attributes(query, Select(Property))
        expectedValue = Select(Property).where(Property.price <= 100000)
        self.assertEqual(str(conditions), str(expectedValue))
    
    def test_condition_bedrooms_min(self):
        query = PropertyQuery(bedrooms_min=2) # type: ignore
        conditions = set_attributes(query, Select(Property))
        expectedValue = Select(Property).where(Property.bedrooms >= 2)
        self.assertEqual(str(conditions), str(expectedValue))
    
    def test_condition_bedrooms_max(self):
        query = PropertyQuery(bedrooms_max=2) # type: ignore
        conditions = set_attributes(query, Select(Property))
        expectedValue = Select(Property).where(Property.bedrooms <= 2)
        self.assertEqual(str(conditions), str(expectedValue))
    
    def test_condition_bathroom_min(self):
        query = PropertyQuery(bathroom_min=2) # type: ignore
        conditions = set_attributes(query, Select(Property))
        expectedValue = Select(Property).where(Property.bathrooms >= 2)
        self.assertEqual(str(conditions), str(expectedValue))
    
    def test_condition_bathroom_max(self):
        query = PropertyQuery(bathroom_max=2) # type: ignore
        conditions = set_attributes(query, Select(Property))
        expectedValue = Select(Property).where(Property.bathrooms <= 2)
        self.assertEqual(str(conditions), str(expectedValue))

    def test_condition_square_meters_min(self):
        query = PropertyQuery(square_meters_min=30) # type: ignore
        conditions = set_attributes(query, Select(Property))
        expectedValue = Select(Property).where(Property.square_meters >= 30)
        self.assertEqual(str(conditions), str(expectedValue))

    def test_condition_square_meters_max(self):
        query = PropertyQuery(square_meters_max=30) # type: ignore
        conditions = set_attributes(query, Select(Property))
        expectedValue = Select(Property).where(Property.square_meters <= 30)
        self.assertEqual(str(conditions), str(expectedValue))

    def test_condition_year_built_from(self):
        query = PropertyQuery(year_built_from=2000) # type: ignore
        conditions = set_attributes(query, Select(Property))
        expectedValue = Select(Property).where(Property.year_built >= 2000)
        self.assertEqual(str(conditions), str(expectedValue))

    def test_condition_year_built_to(self):
        query = PropertyQuery(year_built_to=2000) # type: ignore
        conditions = set_attributes(query, Select(Property))
        expectedValue = Select(Property).where(Property.year_built <= 2000)
        self.assertEqual(str(conditions), str(expectedValue))

    def test_condition_property_type(self):
        query = PropertyQuery(property_type=PropertyType.HOUSE) # type: ignore
        conditions = set_attributes(query, Select(Property))
        expectedValue = Select(Property).where(Property.property_type == PropertyType.HOUSE.value)
        self.assertEqual(str(conditions), str(expectedValue))

    def test_condition_location(self):
        query = PropertyQuery(location=SwissCities.ZURICH) # type: ignore
        conditions = set_attributes(query, Select(Property))
        expectedValue = Select(Property).where(Property.location == SwissCities.ZURICH.value)
        self.assertEqual(str(conditions), str(expectedValue))

    def test_double_condition(self):
        query = PropertyQuery(price_min=100000, price_max=200000) # type: ignore
        conditions = set_attributes(query, Select(Property))
        expectedValue = Select(Property).where(Property.price >= 100000).where(Property.price <= 200000)
        self.assertEqual(str(conditions), str(expectedValue))

    def test_pagination_limit(self):
        query = PropertyQuery(limit=10) # type: ignore
        conditions = set_pagination(query, Select(Property))
        expectedValue = Select(Property).limit(10)
        self.assertEqual(str(conditions), str(expectedValue))
    
    def test_pagination_offset(self):
        query = PropertyQuery(offset=23) # type: ignore
        conditions = set_pagination(query, Select(Property))
        expectedValue = Select(Property).limit(-1).offset(23)
        self.assertEqual(str(conditions), str(expectedValue))
    
    def test_pagination(self):
        query = PropertyQuery(limit=10, offset=23) # type: ignore
        conditions = set_pagination(query, Select(Property))
        expectedValue = Select(Property).limit(10).offset(23)
        self.assertEqual(str(conditions), str(expectedValue))

    def test_order_price_asc(self):
        query = PropertyQuery(order=ResultOrder.PRICE_ASC) # type: ignore
        conditions = set_order(query, Select(Property))
        expectedValue = Select(Property).order_by(Property.price)
        self.assertEqual(str(conditions), str(expectedValue))

    def test_order_price_desc(self):
        query = PropertyQuery(order=ResultOrder.PRICE_DESC) # type: ignore
        conditions = set_order(query, Select(Property))
        expectedValue = Select(Property).order_by(Property.price.desc())
        self.assertEqual(str(conditions), str(expectedValue))

    def test_order_bathroom_asc(self):
        query = PropertyQuery(order=ResultOrder.BATHROOMS_ASC) # type: ignore
        conditions = set_order(query, Select(Property))
        expectedValue = Select(Property).order_by(Property.bathrooms)
        self.assertEqual(str(conditions), str(expectedValue))

    def test_order_bathroom_desc(self):
        query = PropertyQuery(order=ResultOrder.BATHROOMS_DESC) # type: ignore
        conditions = set_order(query, Select(Property))
        expectedValue = Select(Property).order_by(Property.bathrooms.desc())
        self.assertEqual(str(conditions), str(expectedValue))

    def test_order_bedroom_asc(self):
        query = PropertyQuery(order=ResultOrder.BEDROOMS_ASC) # type: ignore
        conditions = set_order(query, Select(Property))
        expectedValue = Select(Property).order_by(Property.bedrooms)
        self.assertEqual(str(conditions), str(expectedValue))

    def test_order_bedroom_desc(self):
        query = PropertyQuery(order=ResultOrder.BEDROOMS_DESC) # type: ignore
        conditions = set_order(query, Select(Property))
        expectedValue = Select(Property).order_by(Property.bedrooms.desc())
        self.assertEqual(str(conditions), str(expectedValue))

    def test_order_sqmt_asc(self):
        query = PropertyQuery(order=ResultOrder.SQUARE_METERS_ASC) # type: ignore
        conditions = set_order(query, Select(Property))
        expectedValue = Select(Property).order_by(Property.square_meters)
        self.assertEqual(str(conditions), str(expectedValue))
    
    def test_order_sqmt_desc(self):
        query = PropertyQuery(order=ResultOrder.SQUARE_METERS_DESC) # type: ignore
        conditions = set_order(query, Select(Property))
        expectedValue = Select(Property).order_by(Property.square_meters.desc())
        self.assertEqual(str(conditions), str(expectedValue))

    def test_order_year_built_asc(self):
        query = PropertyQuery(order=ResultOrder.YEAR_BUILT_ASC) # type: ignore
        conditions = set_order(query, Select(Property))
        expectedValue = Select(Property).order_by(Property.year_built)
        self.assertEqual(str(conditions), str(expectedValue))

    def test_order_year_built_desc(self):
        query = PropertyQuery(order=ResultOrder.YEAR_BUILT_DESC) # type: ignore
        conditions = set_order(query, Select(Property))
        expectedValue = Select(Property).order_by(Property.year_built.desc())
        self.assertEqual(str(conditions), str(expectedValue))