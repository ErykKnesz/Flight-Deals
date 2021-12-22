import os
import smtplib
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_NUMBER = os.environ["TWILIO_NUMBER"]

phone_number = os.environ["phone_number"]
my_email = os.environ["my_email"]
password = os.environ["password"]


class NotificationManager:

    def send_sms(self, message):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages \
            .create(
                body=message,
                from_=TWILIO_NUMBER,
                to=phone_number
            )
        return message

    def send_email(self, message, emails):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            for email in emails:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=email,
                                    msg="Subject: LOW PRICE ALERT \n\n"+message)