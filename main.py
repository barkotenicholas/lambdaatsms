from africastalking import AfricasTalking
from send_sms import SendSms
class Main(AfricasTalking,SendSms):
    def __init__(self):
        super().__init__()
        SendSms().__init__(self)
        self.send_sms = self.send_sms("Today","Phone")
