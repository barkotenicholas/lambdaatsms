import json 

def barkote_send_sms(event,context):
    
    message = 'Hello {}!'.format(event['message'])  

    return {
        'message':message
    }
    