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
    dbSession = get_session()

    def set_db(self, dbSession):
        self.dbSession = dbSession
        return self

    def provide(self, InterestSchema: InterestSchema):
        self.interest = schemaToModelInterest(InterestSchema)
        return self

    def declare(self)-> InterestSchema:
        self.interest.timestamp = datetime.now(tz=timezone.utc)
        try:
            self.dbSession.add(self.interest)
            self.dbSession.commit()
        except IntegrityError as e:
            self.dbSession.rollback()
            self.dbSession.close()
            raise HTTPException(status_code=409, detail=e._message())
        self.dbSession.refresh(self.interest)
        self.dbSession.close()
        return modelToSchemaInterest(self.interest)
    
    def revoke(self):
        deletion_target = self.dbSession.query(InterestModel).filter(
            (InterestModel.propertyId == self.interest.propertyId) &
            (InterestModel.userId == self.interest.userId)
        )
        if(deletion_target.count() == 1):
            deletion_target.delete()
            self.dbSession.commit()
            self.dbSession.close()
        else : # deletion_target.count() == 0
            self.dbSession.close()
            detail_literal = f"Item with propertyID {self.interest.propertyId} and user {self.interest.userId} not found";
            raise HTTPException(status_code=404, detail=detail_literal)
        
    def fetch_by_user(self, userId: str) -> List[InterestSchema]:
        interestsModel = self.dbSession.query(InterestModel).filter(InterestModel.userId == userId).all()
        self.dbSession.close()
        interests = []
        for interestModel in interestsModel:
            interests.append(modelToSchemaInterest(interestModel))
        return interests
    
    def fetch_by_property(self, propertyId: int) -> List[InterestSchema]:
        interestsModel = self.dbSession.query(InterestModel).filter(InterestModel.propertyId == propertyId).all()
        self.dbSession.close()
        interests = []
        for interestModel in interestsModel:
            interests.append(modelToSchemaInterest(interestModel))
        return interests
    