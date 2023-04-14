import boto3

def lambda_handler(event, context):
    # Create a DynamoDB client
    dynamodb = boto3.resource('dynamodb')

    # Get the DynamoDB table
    table = dynamodb.Table('your_table_name')

    # Define the new item to add to the table
    new_item = {
        'your_primary_key_name': 'your_primary_key_value',
        'your_attribute_name': 'your_attribute_value',
        # Add additional attributes as needed
    }

    # Add the new item to the table
    table.put_item(Item=new_item)

    # Return a success message as the response of the Lambda function
    return {
        'statusCode': 200,
        'body': 'Item added to DynamoDB table'
    }
