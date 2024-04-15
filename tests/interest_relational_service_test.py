import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import create_autospec
from sqlalchemy.orm import Session
from app.services.interest_relational_service import InterestService
from app.schemas.interest import Interest as InterestSchema
from app.models.interest import Interest as InterestModel
from datetime import datetime
from datetime import timezone
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

class TestInterestService(unittest.TestCase):

    def test_declare_sunny(self):
        # Arrange
        mock_session = create_autospec(Session, instance=True)

        # Act
        interest = InterestService()
        interest.provide(InterestSchema(propertyId=1, userId="user1", timestamp=None))
        result = interest.declare(db=mock_session)

        # Assert
        self.assertEqual(result.propertyId, 1)
        self.assertEqual(result.userId, "user1")
        self.assertIsNotNone(result.timestamp)

    def test_declare_integrity_error(self):
        # Arrange
        mock_session = create_autospec(Session, instance=True)
        mock_session.add.side_effect = IntegrityError(statement=None, params=None, orig=BaseException(), connection_invalidated=False)

        # Act
        interest = InterestService()
        interest.provide(InterestSchema(propertyId=1, userId="user1", timestamp=None))

        # Assert
        with self.assertRaises(HTTPException):
            interest.declare(db=mock_session)

    def test_revoke_sunny(self):
        # Arrange
        mock_session = create_autospec(Session, instance=True)
        mock_query = mock_session.query.return_value
        mock_query.filter.return_value.count.return_value = 1

        # Act
        interest = InterestService()
        interest.provide(InterestSchema(propertyId=1, userId="user1", timestamp=None))
        interest.revoke(db=mock_session)

        # Assert
        mock_session.commit.assert_called_once()

    def test_revoke_not_found(self):
        # Arrange
        mock_session = create_autospec(Session, instance=True)
        mock_query = mock_session.query.return_value
        mock_query.filter.return_value.count.return_value = 0

        # Act
        interest = InterestService()
        interest.provide(InterestSchema(propertyId=1, userId="user1", timestamp=None))

        # Assert
        with self.assertRaises(HTTPException):
            interest.revoke(db=mock_session)

    def test_fetch_by_user(self):
        # Arrange
        mock_session = create_autospec(Session, instance=True)
        mock_query = mock_session.query.return_value
        mock_query.filter.return_value.all.return_value = [InterestModel(propertyId=1, userId="user1", timestamp=datetime.now(tz=timezone.utc))]
        
        # Act
        result = InterestService().fetch_by_user("user1", db=mock_session)

        # Assert
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].propertyId, 1)
        self.assertEqual(result[0].userId, "user1")
        self.assertIsNotNone(result[0].timestamp)

    def test_fetch_by_property(self):
        # Arrange
        mock_session = create_autospec(Session, instance=True)
        mock_query = mock_session.query.return_value
        mock_query.filter.return_value.all.return_value = [InterestModel(propertyId=1, userId="user1", timestamp=datetime.now(tz=timezone.utc))]
        
        # Act
        result = InterestService().fetch_by_property(1, db=mock_session)

        # Assert
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].propertyId, 1)
        self.assertEqual(result[0].userId, "user1")
        self.assertIsNotNone(result[0].timestamp)
