import boto3

session = boto3.Session(
    aws_access_key_id='dummy',
    aws_secret_access_key='dummy',
    region_name='us-west-2'
)

dynamodb = session.resource('dynamodb', 
                          endpoint_url='http://dynamodb-local:8000', use_ssl=False)

def delete_table(dynamodb, table_name):
    try:
        table = dynamodb.Table(table_name)
        table.delete()
        print(f"Table {table_name} deleted successfully.")
    except Exception as e:
        print(f"Error deleting table {table_name}.", e)

delete_table(dynamodb, 'PropertyTable')