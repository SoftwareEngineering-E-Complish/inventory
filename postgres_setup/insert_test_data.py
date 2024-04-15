import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.property_relational_service import insert_property
from app.services.interest_relational_service import InterestService
from app.schemas.property import Property
from app.schemas.interest import Interest
from app.utils.entity_mapper import schemaToModel
import pandas as pd

def load_property_test_data():
    # load and create property instances from the test data
    df = pd.read_csv('./postgres_setup/property_test_data.csv')
    properties = []
    for _, row in df.iterrows():
        properties.append(Property(**row.to_dict()))
    for property in properties:
        insert_property(schemaToModel(property))
    return

def load_interest_test_data():
    # load and create interest instances from the test data
    df = pd.read_csv('./postgres_setup/interest_test_data.csv')
    interest_list = []
    for _, row in df.iterrows():
        interest_list.append(Interest(**row.to_dict()))
    for interest in interest_list:
        interestService = InterestService()
        interestService.provide(interest)
        interestService.declare()
    return

load_property_test_data()
load_interest_test_data()