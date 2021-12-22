import requests

SHEETY_PRICES_ENDPOINT = ("https://api.sheety.co/23cbaa2478e458e06e8b4bf24e02f0ba/"
                         "eryksFlightDeals/prices")


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        resp = requests.get(SHEETY_PRICES_ENDPOINT)
        data = resp.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_rows(self, object_id, data):
        endpoint = f"{SHEETY_PRICES_ENDPOINT}/{object_id}"
        headers = {
            "Content-Type": "application/json"
        }
        r = requests.put(endpoint, json=data, headers=headers)
        return r.text


