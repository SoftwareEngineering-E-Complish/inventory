import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from app.models.property import Property as PropertyModel
from app.schemas.property import Property as PropertySchema
from app.schemas.property import PropertyType
from app.utils.entity_mapper import schemaToModel, modelToSchema

class TestEntityMapper(unittest.TestCase):

    def test_schemaToModel(self):
        schema = PropertySchema(bedrooms=2, bathrooms=1, property_type=PropertyType.APARTMENT)
        model = schemaToModel(schema)
        self.assertEqual(model.bedrooms, 2)
        self.assertEqual(model.bathrooms, 1)
        self.assertEqual(model.property_type, PropertyType.APARTMENT.value)

    def test_modelToSchema(self):
        model = PropertyModel(bedrooms=2, bathrooms=1, property_type=PropertyType.APARTMENT.value)
        schema = modelToSchema(model)
        self.assertEqual(schema.bedrooms, 2)
        self.assertEqual(schema.bathrooms, 1)
        self.assertEqual(schema.property_type, PropertyType.APARTMENT)
