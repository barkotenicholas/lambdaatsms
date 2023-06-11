from africas_talking import AfricasTalking
import africastalking as at
class SendSms(AfricasTalking):
    def __init__(self):
        super().__init__()
        self.sms = at.SMS

