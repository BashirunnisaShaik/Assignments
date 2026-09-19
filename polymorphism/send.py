class EmailNotification:
    def send(self):
        print("Sending Email")
class SMSNotification:
    def send(self):
        print("Sending SMS")
email=EmailNotification()
sms=SMSNotification()
email.send()
sms.send()