import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.property_relational_service import insert_property
from app.schemas.property import Property
from app.utils.entity_mapper import schemaToModel
import pandas as pd

def load_test_data():
    # load and create property instances from the test data
    df = pd.read_csv('./postgres_setup/test_data.csv')
    properties = []
    for _, row in df.iterrows():
        properties.append(Property(**row.to_dict()))
    for property in properties:
        insert_property(schemaToModel(property))
    return

load_test_data()