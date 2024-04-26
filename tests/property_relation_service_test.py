import unittest
from unittest.mock import create_autospec
from sqlalchemy.orm import Session
from app.models.property import Property
from app.schemas.property_query import PropertyQuery
from app.services.property_relational_service import PropertyService

class TestPropertyService(unittest.TestCase):

    def test_insert_property(self):
    # Arrange
        mock_session = create_autospec(Session, instance=True)
        property = Property(propertyId=None, price=100000, bedrooms=2, bathrooms=2, square_meters=30, 
                            year_built=2000, owner="user1")

        # Act
        propertyService = PropertyService()
        propertyService.set_session(mock_session).insert_property(property)

        # Assert
        mock_session.add.assert_called_once_with(property)
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once_with(property)

    def test_fetch_property(self):
        # Arrange
        mock_session = create_autospec(Session, instance=True)
        mock_session.execute.return_value.scalars.return_value.first.return_value = Property(
            propertyId=1, price=100000, bedrooms=2, bathrooms=2, square_meters=30, year_built=2000, owner="user1")

        # Act
        propertyService = PropertyService()
        result = propertyService.set_session(mock_session).fetch_property(1)

        # Assert
        self.assertEqual(result.propertyId, 1)
        self.assertEqual(result.price, 100000)
        self.assertEqual(result.bedrooms, 2)
        self.assertEqual(result.bathrooms, 2)
        self.assertEqual(result.square_meters, 30)
        self.assertEqual(result.year_built, 2000)
        self.assertEqual(result.owner, "user1")

    def test_fetch_all(self):
        # Arrange
        mock_session = create_autospec(Session, instance=True)
        mock_session.execute.return_value.scalars.return_value.all.return_value = [
            Property(propertyId=1, bedrooms=2),
            Property(propertyId=2, bedrooms=3)]

        # Act
        propertyService = PropertyService()
        result = propertyService.set_session(mock_session).fetch_all()

        # Assert
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].propertyId, 1)
        self.assertEqual(result[1].propertyId, 2)

    def test_fetch_by_user(self):
        # Arrange
        mock_session = create_autospec(Session, instance=True)
        mock_session.execute.return_value.scalars.return_value.all.return_value = [
            Property(propertyId=1, owner="user1"),
            Property(propertyId=2, owner="user1")]

        # Act
        result = PropertyService().set_session(mock_session).fetch_by_user("user1")

        # Assert
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].propertyId, 1)
        self.assertEqual(result[1].propertyId, 2)

    def test_fetch_by_attributes(self):
        mock_session = create_autospec(Session, instance=True)
        mock_session.execute.return_value.scalar.return_value = 2
        mock_session.execute.return_value.scalars.return_value.all.return_value = [
            Property(propertyId=1, price=100000, bedrooms=2),
            Property(propertyId=2, price=200000, bedrooms=3)]
        
        # Act
        result, count = PropertyService().set_session(mock_session).fetch_by_attributes(
            PropertyQuery(bedrooms_min=2))
        
        # Assert
        self.assertEqual(count, 2)
        self.assertEqual(result[0].propertyId, 1)
        self.assertEqual(result[1].propertyId, 2)

    def test_update_property(self):
        # Arrange
        mock_session = create_autospec(Session, instance=True)
        property = Property(propertyId=1, price=100000, bedrooms=2, bathrooms=2, square_meters=30, 
                            year_built=2000, owner="user1")
        mock_session.execute.return_value.scalars.return_value.first.return_value = property
        updated_property = Property(propertyId=2, price=200000, bedrooms=3, owner="user2")

        # Act
        propertyService = PropertyService()
        propertyService.set_session(mock_session).update_property(1, updated_property)

        # Assert
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once_with(property)
        self.assertEqual(property.propertyId, 1)
        #Assert key is ignored
        self.assertEqual(property.price, 200000)
        #Assert user is ignored
        self.assertEqual(property.owner, "user1")
        #Assert other fields are updated
        self.assertEqual(property.bedrooms, 3)