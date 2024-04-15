from sqlalchemy import create_engine, select, func, Select, Sequence
from app.models.interest import Interest as InterestModel
from app.schemas.interest import Interest as InterestSchema
from app.utils.entity_mapper_interest import schemaToModelInterest, modelToSchemaInterest
from app.utils.db_connector import get_session
from datetime import datetime
from datetime import timezone
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from typing import List

class InterestService():
    interest: InterestModel

    def provide(self, InterestSchema: InterestSchema):
        self.interest = schemaToModelInterest(InterestSchema)

    def declare(self)-> InterestSchema:
        self.interest.timestamp = datetime.now(tz=timezone.utc)
        db = get_session()
        try:
            db.add(self.interest)
            db.commit()
        except IntegrityError as e:
            db.rollback()
            db.close()
            raise HTTPException(status_code=409, detail=e._message())
        db.refresh(self.interest)
        db.close()
        return modelToSchemaInterest(self.interest)
    
    def revoke(self):
        db = get_session()
        deletion_target = db.query(InterestModel).filter(
            (InterestModel.propertyId == self.interest.propertyId) &
            (InterestModel.userId == self.interest.userId)
        )
        if(deletion_target.count() == 1):
            deletion_target.delete()
            db.commit()
            db.close()
        elif (deletion_target.count() == 0):
            db.close()
            detail_literal = f"Item with propertyID {self.interest.propertyId} and user {self.interest.userId} not found";
            raise HTTPException(status_code=404, detail=detail_literal)
        
    def fetch_by_user(self, userId: str) -> List[InterestSchema]:
        db = get_session()
        interestsModel = db.query(InterestModel).filter(InterestModel.userId == userId).all()
        db.close()
        interests = []
        for interestModel in interestsModel:
            interests.append(modelToSchemaInterest(interestModel))
        return interests
    
    def fetch_by_property(self, propertyId: int) -> List[InterestSchema]:
        db = get_session()
        interestsModel = db.query(InterestModel).filter(InterestModel.propertyId == propertyId).all()
        db.close()
        interests = []
        for interestModel in interestsModel:
            interests.append(modelToSchemaInterest(interestModel))
        return interests