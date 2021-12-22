import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]


class NotificationManager:
    def send_notification(self, price, from_city, from_airport, to_city,
                          to_airport, out_date, return_date):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
                body=f"Low price alert! Only {price} GBP to fly from"
                     f" {from_city}-{from_airport} to {to_city}-{to_airport}"
                     f"from {out_date} to {return_date}",
                from_="+19203974062",
                to="+48511755446"
            )
        return message