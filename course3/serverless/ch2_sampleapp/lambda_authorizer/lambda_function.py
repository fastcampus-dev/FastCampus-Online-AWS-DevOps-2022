import jwt
import json

def lambda_handler(event, context):
    token = event['headers']['Authorization']
    secret = '1nHhM7Ex+2d0uIsJhU/EqHCzs5aIKToRoX9oPECGUbDdabhudB/vcckfMD/4wJ6dT2V2fsvUqbdgEBBUcWhebslWsbzoX4PE+cpPR6Uy9IV3sZiiNAp8Pb92qBW1jqrfn0kay2v+Yk11a5C7/9v5gjOkwcvAHmzsci7p6we5ZV2GamNANmolONya4fGibZcANacsXz0XvzZcce9a4pNv0XeLGNm1Rnsrl2KH/uOAIujCEJazl7Dsbx2RN43wX/J3OD/Coko7uYU4pWQ831O2q31T5PqxdcWUOpqkUcpoeDbisnpnQ22dVSvN6Ixe2l8PJ6cTqomULiL7k/2Cxf5VOg=='  # replace with your own secret key

    try:
        # Decode the JWT token
        decoded_token = jwt.decode(token, secret, algorithms=['HS256'])
        user_id = decoded_token['user_id']  # assuming user_id is a field in the token
    except:
        # If the token is invalid, return a 401 Unauthorized response
        return {
            'statusCode': 401,
            'body': json.dumps({'message': 'Unauthorized'})
        }

    # If the token is valid, allow the request to proceed with the user_id as the principal
    return {
        'principalId': user_id,
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': 'execute-api:Invoke',
                    'Effect': 'Allow',
                    'Resource': event['methodArn']
                }
            ]
        }
    }
