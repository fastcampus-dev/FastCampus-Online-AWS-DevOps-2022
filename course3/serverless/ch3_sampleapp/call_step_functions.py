import json
import boto3

def lambda_handler(event, context):
    
    # Create an AWS Step Functions client
    sf_client = boto3.client('stepfunctions')
    
    # Define the ARN of the Step Function to call
    state_machine_arn = '<ARN of your Step Function>'
    
    # Define the input for the Step Function (if any)
    input_data = {
        'key1': 'value1',
        'key2': 'value2'
    }
    
    # Call the Step Function using the client and ARN
    response = sf_client.start_execution(
        stateMachineArn=state_machine_arn,
        input=json.dumps(input_data)
    )
    
    # Print the response from the Step Function
    print(response)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Step Function called successfully!')
    }
