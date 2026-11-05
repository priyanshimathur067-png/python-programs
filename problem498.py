class EmailNotification:
    def send_notification(self):
        print("Sending Email Notification")


class SMSNotification:
    def send_notification(self):
        print("Sending SMS Notification")


class WhatsAppNotification:
    def send_notification(self):
        print("Sending WhatsApp Notification")


def send(obj):
    obj.send_notification()


e1 = EmailNotification()
s1 = SMSNotification()
w1 = WhatsAppNotification()

send(e1)
send(s1)
send(w1)