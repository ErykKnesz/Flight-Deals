import requests

SHEETY_PRICES_ENDPOINT = ("https://api.sheety.co/23cbaa2478e458e06e8b4bf24e02f0ba/"
                          "eryksFlightDeals/prices")
SHEETY_USERS_ENDPOINT = ("https://api.sheety.co/23cbaa2478e458e06e8b4bf24e02f0ba/"
                         "eryksFlightDeals/users")


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        resp = requests.get(SHEETY_PRICES_ENDPOINT)
        data = resp.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def update_rows(self, object_id, data):
        endpoint = f"{SHEETY_PRICES_ENDPOINT}/{object_id}"
        headers = {
            "Content-Type": "application/json"
        }
        r = requests.put(endpoint, json=data, headers=headers)
        return r.text

    def add_user(self, first_name, last_name, email):
        user = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        headers = {
            "Content-Type": "application/json"
        }
        r = requests.post(SHEETY_USERS_ENDPOINT, json=user, headers=headers)
        print(r.status_code, r.text)

    def get_users_data(self):
        headers = {
            "Content-Type": "application/json"
        }
        r = requests.get(SHEETY_USERS_ENDPOINT, headers=headers)

        return r.json()["users"]
