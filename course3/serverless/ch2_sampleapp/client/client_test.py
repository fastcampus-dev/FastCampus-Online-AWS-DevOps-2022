import boto3
import json
import requests

# Replace with your own Lambda Authorizer ARN and API Gateway endpoint
AUTHORIZER_ARN = 'arn:aws:lambda:ap-northeast-2:856517815076:function:lambdaAuthorizer'
ENDPOINT = 'https://evxwnn1aca.execute-api.ap-northeast-2.amazonaws.com/forum'

# Replace with your own JWT token
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiQm9yYW0gSmVvbmcifQ.TPQHFjGctA6NZfeTnfm1CqnoN7Vx5TPOL60DXvZQt30'

# Create a Boto3 client for invoking Lambda functions
lambda_client = boto3.client('lambda')

# Invoke the Lambda Authorizer with the JWT token
response = lambda_client.invoke(
    FunctionName=AUTHORIZER_ARN,
    InvocationType='RequestResponse',
    Payload='{"headers": {"Authorization": "%s"}, "methodArn": "%s"}' % (TOKEN, ENDPOINT)
)

# Parse the response from the Lambda Authorizer
auth_response = response['Payload'].read().decode('utf-8')
auth_response = json.loads(auth_response)

print(auth_response)

# Check if the request is authorized
if auth_response['policyDocument']['Statement'][0]['Effect'] == 'Allow':
    # If authorized, make a request to the API Gateway endpoint with the JWT token
    headers = {'Authorization': TOKEN}
    response = requests.get(ENDPOINT, headers=headers)
    print(response.text)
else:
    # If unauthorized, print an error message
    print('Unauthorized')
