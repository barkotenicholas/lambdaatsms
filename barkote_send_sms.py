from send_sms import SendSms
from africas_talking import AfricasTalking
def barkote_send_sms(event,context):
    
    main = AfricasTalking()

    response = main.send_sms(event['message'],event['number'])

    print(response)
    return {
        'message':response
    }