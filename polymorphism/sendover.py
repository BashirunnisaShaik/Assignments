class Notification:
    def send(self):
        print("Sending notification")
class Email(Notification):
    def send(self):
        print("Sending Email")
class SMS(Notification):
    def send(self):
        print("Sending SMS")
class WhatsApp(Notification):
    def send(self):
        print("Sending WhatsApp message")
Email().send()
SMS().send()
WhatsApp().send()