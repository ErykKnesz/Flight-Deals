import requests
from datetime import datetime, timedelta

TEQUILA_API_KEY = "I81Zo-QpNuGv1Lz1HekGPpk-PEMqKsob"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

class FlightSearch:

    def get_iata_code(self, term):
        params = {
            "term": term,
            "location_types": "airport"
        }
        headers = {
            "apikey": TEQUILA_API_KEY,
            "accept": "application / json"
        }
        endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        r = requests.get(endpoint, params=params, headers=headers)
        r = r.json()["locations"][0]
        return r["city"]["code"]

    def get_cheapest_flight(self, my_place, destination, max_stay=(6 * 30)):
        tomorrow = datetime.now() + timedelta(days=1)
        params = {
            "fly_from": my_place,
            "fly_to": destination['iataCode'],
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": (tomorrow + timedelta(days=max_stay)
                        ).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }
        headers = {
            "apikey": TEQUILA_API_KEY,
            "accept": "application / json"
        }
        endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        r = requests.get(endpoint, params=params, headers=headers)
        try:
            data = r.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination}.")
            return None
        return data