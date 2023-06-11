import json 
from send_sms import SendSms
def barkote_send_sms(event,context):
    
    message = 'Hello {}!'.format(event['message'])  

    main = SendSms()

    response = main.send_sms("Hello","sdas")

    return {
        'message':message
    }
    