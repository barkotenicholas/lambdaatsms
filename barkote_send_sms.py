import boto3
import json
def barkote_send_sms(event,context):
    
    client = boto3.client("sts")
    response = client.assume_role(
        RoleArn="arn:aws:iam::455435218184:role/crossaccountrole",
        RoleSessionName="practise"
    )
    ACCESS_KEY = response['Credentials']['AccessKeyId']
    SECRET_KEY = response['Credentials']['SecretAccessKey']
    SESSION_TOKEN = response['Credentials']['SessionToken']

 
    return {
        "status":200,
        "list":"list_of_files"
    }
        
