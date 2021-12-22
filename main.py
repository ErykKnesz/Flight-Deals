from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

for city in sheet_data:
    flight = flight_search.get_cheapest_flight(ORIGIN_CITY_IATA, city)
    new_flight = FlightData(
        price=flight["price"],
        departure_airport_code=flight["route"][0]["flyFrom"],
        departure_city=flight["route"][0]["cityFrom"],
        departure_city_code=flight["route"][0]["cityCodeFrom"],
        destination_city=flight["route"][0]["cityTo"],
        destination_city_code=flight["route"][0]["cityCodeTo"],
        destination_airport_code=flight["route"][0]["flyTo"],
        out_date=flight["route"][0]["local_departure"].split("T")[0],
        return_date=flight["route"][1]["local_departure"].split("T")[0]
    )

    if new_flight.price < city["lowestPrice"]:
        notification_manager.send_notification(
            price=new_flight.price,
            from_city=new_flight.departure_city,
            from_airport=new_flight.departure_airport_code,
            to_city=new_flight.destination_city,
            to_airport=new_flight.destination_airport_code,
            out_date=new_flight.out_date,
            return_date=new_flight.return_date
        )
    pprint(sheet_data)
