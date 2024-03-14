import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from boto3.dynamodb.conditions import Attr
from app.models.property_query import PropertyQuery
from app.models.property import PropertyType, SwissCities
from app.services.property_service import parse_property_query

# This test case is to test the condition expression for the scan operation
class TestPropertyQuery(unittest.TestCase):
    baseCondition = Attr('propertyId').exists()

    def test_condition_empty(self):
        query = PropertyQuery()
        conditions = parse_property_query(query)
        self.assertEqual(conditions, self.baseCondition)

    def test_condition_price_min(self):
        query = PropertyQuery(price_min=100000)
        conditions = parse_property_query(query)
        self.assertEqual(conditions, self.baseCondition & Attr('price').gte(100000))
    
    def test_condition_price_max(self):
        query = PropertyQuery(price_max=100000)
        conditions = parse_property_query(query)
        self.assertEqual(conditions, self.baseCondition & Attr('price').lte(100000))
    
    def test_condition_bedrooms_min(self):
        query = PropertyQuery(bedrooms_min=2)
        conditions = parse_property_query(query)
        self.assertEqual(conditions, self.baseCondition & Attr('bedrooms').gte(2))
    
    def test_condition_bedrooms_max(self):
        query = PropertyQuery(bedrooms_max=2)
        conditions = parse_property_query(query)
        self.assertEqual(conditions, self.baseCondition & Attr('bedrooms').lte(2))
    
    def test_condition_bathroom_min(self):
        query = PropertyQuery(bathroom_min=1)
        conditions = parse_property_query(query)
        self.assertEqual(conditions, self.baseCondition & Attr('bathrooms').gte(1))
    
    def test_condition_bathroom_max(self):
        query = PropertyQuery(bathroom_max=2)
        conditions = parse_property_query(query)
        self.assertEqual(conditions, self.baseCondition & Attr('bathrooms').lte(2))

    def test_condition_square_meters_min(self):
        query = PropertyQuery(square_meters_min=30)
        conditions = parse_property_query(query)
        self.assertEqual(conditions, self.baseCondition & Attr('square_meters').gte(30))

    def test_condition_square_meters_max(self):
        query = PropertyQuery(square_meters_max=30)
        conditions = parse_property_query(query)
        self.assertEqual(conditions, self.baseCondition & Attr('square_meters').lte(30))

    def test_condition_year_built_from(self):
        query = PropertyQuery(year_built_from=2000)
        conditions = parse_property_query(query)
        self.assertEqual(conditions, self.baseCondition & Attr('year_built').gte(2000))

    def test_condition_year_built_to(self):
        query = PropertyQuery(year_built_to=2000)
        conditions = parse_property_query(query)
        self.assertEqual(conditions, self.baseCondition & Attr('year_built').lte(2000))

    def test_condition_property_type(self):
        query = PropertyQuery(property_type=PropertyType.HOUSE)
        conditions = parse_property_query(query)
        self.assertEqual(conditions, self.baseCondition & Attr('property_type').eq(PropertyType.HOUSE.value))

    def test_condition_location(self):
        query = PropertyQuery(location=SwissCities.ZURICH)
        conditions = parse_property_query(query)
        self.assertEqual(conditions, self.baseCondition & Attr('location').eq(SwissCities.ZURICH.value))

    def double_condition(self):
        query = PropertyQuery(price_min=100000, price_max=200000)
        conditions = parse_property_query(query)
        self.assertEqual(conditions, self.baseCondition & Attr('price').gte(100000) & Attr('price').lte(200000))