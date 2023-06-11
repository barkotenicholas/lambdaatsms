import json 

def barkote_send_sms(event,context):
    
    message = event['message']    

    return {
        'message':message
    }
    