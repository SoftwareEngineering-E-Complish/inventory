import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from app.models.interest import Interest as InterestModel
from app.schemas.interest import Interest as InterestSchema
from app.utils.entity_mapper_interest import schemaToModelInterest, modelToSchemaInterest

class TestEntityMapperInterest(unittest.TestCase):

    def test_schemaToModelInterest(self):
        schema = InterestSchema(propertyId=1, userId="user1", timestamp=None)
        model = schemaToModelInterest(schema)

        self.assertEqual(model.propertyId, 1)
        self.assertEqual(model.userId, "user1")
        self.assertEqual(model.timestamp, None)

    def test_modelToSchemaInterest(self):
        model = InterestModel(propertyId=1, userId="user1", timestamp=None)
        schema = schemaToModelInterest(model)

        self.assertEqual(schema.propertyId, 1)
        self.assertEqual(schema.userId, "user1")
        self.assertEqual(schema.timestamp, None)
