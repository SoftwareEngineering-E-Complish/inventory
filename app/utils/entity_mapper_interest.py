from app.models.interest import Interest as InterestModel
from app.schemas.interest import Interest as InterestSchema

def schemaToModelInterest(interestSchema: InterestSchema) -> InterestModel:
    modelInterest = InterestModel()
    #modelInterest.interestId = interestSchema.interestId #type: ignore
    modelInterest.propertyId = interestSchema.propertyId #type: ignore
    modelInterest.userId = interestSchema.userId #type: ignore
    modelInterest.timestamp = interestSchema.timestamp #type: ignore
    return modelInterest

def modelToSchemaInterest(modelInterest: InterestModel) -> InterestSchema:
    return InterestSchema(
        #interestId = modelInterest.interestId, #type: ignore
        propertyId = modelInterest.propertyId, #type: ignore
        userId = modelInterest.userId, # type: ignore
        timestamp = modelInterest.timestamp); #type: ignore