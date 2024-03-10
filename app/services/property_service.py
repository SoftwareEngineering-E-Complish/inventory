import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Attr, And
from fastapi import HTTPException
import uuid
from app.models.property import Property

dynamodb = boto3.resource('dynamodb', 
                          region_name='us-west-2', 
                          endpoint_url='http://dynamodb-local:8000',
                          aws_access_key_id='dummy',
                          aws_secret_access_key='dummy')

table = dynamodb.Table('PropertyTable')

def create_property_autoKey(property:Property):
    property_id = str(uuid.uuid4())  # Generate a UUID
    property.propertyId = property_id  # Set the propertyId to the generated UUID
    print("Before put_item:" + property.model_dump().__str__())

    existing_property = get_property(property_id)
    if existing_property:
        raise HTTPException(status_code=400, detail="Property already exists")
    try:

        response = table.put_item(Item=property.model_dump())
        return property  # Return the created property itself
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_property(propertyId):
    try:
        response = table.get_item(Key={'propertyId': propertyId})
    except ClientError as e:
        print("Error Message:" + e.response['Error']['Message'])
        return None
    item = response.get('Item', None)
    if item is not None:
        return Property(**item)
    else:
        return None

def get_all_properties():
    response = table.scan()
    return response.get('Items', [])


def get_properties_by_attributes(property: Property):
    # Convert the Property object to a dictionary
    property_dict = property.model_dump()

    # Remove None values from the dictionary
    property_dict = {k: v for k, v in property_dict.items() if v is not None and k != 'propertyId'}

    # Create a condition expression for the scan operation
    condition_expression = None
    for key, value in property_dict.items():
        if condition_expression is None:
            condition_expression = Attr(key).eq(value)
        else:
            condition_expression = condition_expression & Attr(key).eq(value)

    # Scan the table with the condition expression
    response = table.scan(FilterExpression=condition_expression)

    # Convert the returned items to Property objects
    properties = [Property(**item) for item in response.get('Items', [])]

    return properties

"""
def update_item(item_id, new_attributes):
    # Check if the item exists before attempting to update
    existing_item = get_property(item_id)
    if not existing_item:
        raise HTTPException(status_code=400, detail="No item found")
    try:
        response = table.update_item(
            Key={'itemId': item_id},
            UpdateExpression='SET title = :title, description = :description, done = :done',
            ExpressionAttributeValues={
                ':title': new_attributes.get('title'),
                ':description': new_attributes.get('description'),
                ':done': new_attributes.get('done')
            },
            ReturnValues='ALL_NEW'
        )
        return response.get('Attributes', {})
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))


def delete_item(item_id):
    try:
        response = table.delete_item(Key={'itemId': item_id})
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return response"""
