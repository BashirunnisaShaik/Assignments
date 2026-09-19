class Email:
    def send(self):
        print("Email sent")
class SMS:
    def send(self):
        print("SMS sent")
class WhatsApp:
    def send(self):
        print("WhatsApp sent")
def send(x):
    x.send()
e=Email()
s=SMS()
w=WhatsApp()
send(e)
send(s)
send(w)