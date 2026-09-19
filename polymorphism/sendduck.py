class EmailService:
    def send(self):
        print("Email sent")
class SMSService:
    def send(self):
        print("SMS sent")
def send(x):
    x.send()
e=EmailService()
s=SMSService()
send(e)
send(s)