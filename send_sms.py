from africastalking import AfricasTalking
class SendSms(AfricasTalking):
    def __init__(self):
        super().__init__()

    def send_sms(self,message,number):
        response = self.sms.send("Hello Message!", ["+254791018766"])
        return response
