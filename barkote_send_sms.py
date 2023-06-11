
import africastalking as at
def barkote_send_sms(event,context):
 
    username = "awssms" 
    api_key = "394957400d15920d7c16a7256387bec89219e3d78e7a40379378916367c7df1f"
    at.initialize(username, api_key)
 
    sms = at.SMS

    response = sms.send(event['message'],[event['number']])

    print(response)
    return {
        'message':response
    }
