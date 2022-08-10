from moesif_aws_lambda import *
import json

def identify_user(event, context):
    return 'my_user_id'

def identify_company(event, context):
    return 'my_company_id'

def get_api_version(event, context):
    return '1.0.0'

def get_session_token(event, context):
    return '23jdf0owekfmcn4u3qypxg09w4d8ayrcdx8nu2ng]s98y18cx98q3yhwmnhcfx43f'

def get_metadata(event, context):
    return { 'foo' : 'aws lambda', 'bar' : 'aws lambda metadata', }

def mask_event(eventmodel):
    return eventmodel

def should_skip(event, context):
    return "skip" in event['path']

moesif_options = {
    'GET_METADATA': get_metadata,
    'IDENTIFY_USER': identify_user,
    'IDENTIFY_COMPANY': identify_company,
    'GET_SESSION_TOKEN': get_session_token,
    'GET_API_VERSION': get_api_version,
    'MASK_EVENT_MODEL': mask_event,
    'LOG_BODY': True,
    'DEBUG': True,
    'SKIP': should_skip,
}

@MoesifLogger(moesif_options)
def lambda_handler(event, context):
     # Outgoing API call to third parties like Github / Stripe or to your own dependencies
    start_capture_outgoing(moesif_options)
    third_party = requests.get('https://httpbin.org/ip', json=json.dumps({'test': 2}),
                               headers={"content-type": "text", "Authorization": "Bearer sdf4854wer"},
                               auth=('Basic', "testauth"))
    return {
        'statusCode': 200,
        'isBase64Encoded': False,
        'body': json.dumps({
            'msg': 'Hello from Lambda!'
            }),
        'headers': {
            'Content-Type': 'application/json'
            }
    }
