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

    # create service client using the assumed role credentials, e.g. S3
    client = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        aws_session_token=SESSION_TOKEN,
    )
    list_of_files = ""

    objects = client.list_objects_v2(Bucket='cloud-cross-accountaccess')

    for obj in objects['Contents']:
        print(obj['Key'])
        list_of_files += obj['Key']
    
    return {
        "status":200,
        "list":list_of_files
    }
        
