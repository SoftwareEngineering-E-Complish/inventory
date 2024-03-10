import boto3

session = boto3.Session(
    aws_access_key_id='dummy',
    aws_secret_access_key='dummy',
    region_name='us-west-2'
)

dynamodb = session.resource('dynamodb', 
                          endpoint_url='http://dynamodb-local:8000', use_ssl=False)

try:
    table = dynamodb.create_table(
        TableName='PropertyTable',
        KeySchema=[
            {
                'AttributeName': 'propertyId',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'propertyId',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print("Table status:", table.table_status)
except Exception as e:
    print('error', e)
