import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.property_service import create_property_autoKey
from app.models.property import Property
import pandas as pd

def load_test_data():
    # load and create property instances from the test data
    df = pd.read_csv('./dynamo_setup/test_data.csv')
    df['propertyId'] = df['propertyId'].astype(str)
    properties = []
    for _, row in df.iterrows():
        properties.append(Property(**row.to_dict()))
    # create_property_autoKey(property:Property)
    for property in properties:
        create_property_autoKey(property)
    return

load_test_data()