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
"""
first_name = input("What is your first name? Enter: ")
last_name = input("What is your last name? Enter: ")
email = input("What is your last email? Enter: ")
email2 = input("Please re-enter your email address. Enter: ")

if email == email2:
    print("Welcome to the Flight Club!")
    data_manager.add_user(first_name, last_name, email)
"""
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

for city in sheet_data:
    flight = flight_search.get_cheapest_flight(ORIGIN_CITY_IATA, city)
    if flight is not None:
        has_stopover = len(flight["route"]) > 2
        destination_city = (flight["route"][1]["cityTo"] if has_stopover
                            else flight["route"][0]["cityTo"])
        destination_airport = (flight["route"][1]["flyTo"] if has_stopover
                               else flight["route"][0]["flyTo"])
        return_date = (flight["route"][2]["local_departure"] if has_stopover
                       else flight["route"][1]["local_departure"])
        new_flight = FlightData(
            price=flight["price"],
            departure_airport_code=flight["route"][0]["flyFrom"],
            departure_city=flight["route"][0]["cityFrom"],
            departure_city_code=flight["route"][0]["cityCodeFrom"],
            destination_city=destination_city,
            destination_city_code=flight["route"][0]["cityCodeTo"],
            destination_airport_code=flight["route"][0]["flyTo"],
            out_date=flight["route"][0]["local_departure"].split("T")[0],
            return_date=flight["route"][1]["local_departure"].split("T")[0]
        )
        message = (f"Low price alert! Only {new_flight.price} GBP to fly from"
                   f" {new_flight.departure_city}-"
                   f"{new_flight.departure_airport_code} to"
                   f" {new_flight.destination_city}-"
                   f"{new_flight.destination_airport_code}"
                   f"from {new_flight.out_date} to {new_flight.return_date}")
        if has_stopover:
            new_flight.stop_overs = 1
            new_flight.via_city = flight["route"][0]["cityTo"]
            message += (f"\nThe flight has {new_flight.stop_overs} stop over"
                        f"via {new_flight.via_city}")

        if new_flight.price < city["lowestPrice"]:
            notification_manager.send_sms(message)
            users = data_manager.get_users_data()
            users_emails = [user["email"] for user in users]
            notification_manager.send_email(message, users_emails)
