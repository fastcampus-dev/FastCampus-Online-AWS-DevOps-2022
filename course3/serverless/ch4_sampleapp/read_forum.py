import boto3

def lambda_handler(event, context):
    # Create a DynamoDB client
    dynamodb = boto3.resource('dynamodb')

    # Get the DynamoDB table
    table = dynamodb.Table('your_table_name')

    # Scan the table to retrieve all the data
    response = table.scan()

    # Extract the items from the response
    items = response.get('Items', [])

    # Continue scanning if the response contains more items
    while 'LastEvaluatedKey' in response:
        last_evaluated_key = response['LastEvaluatedKey']
        response = table.scan(ExclusiveStartKey=last_evaluated_key)
        items.extend(response.get('Items', []))

    # Print the items data
    print(items)

    # Return the items data as the Lambda function's response
    return items
