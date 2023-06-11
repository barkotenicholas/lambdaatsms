import json 
from send_sms import SendSms
def barkote_send_sms(event,context):
    
    message = 'Hello {}!'.format()  

    main = SendSms()

    response = main.send_sms(event['message'],event['number'])

    print(response)
    return {
        'message':response
    }