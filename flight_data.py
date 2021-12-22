class FlightData:
    def __init__(self, price, departure_airport_code, departure_city,
                 departure_city_code, destination_city_code,
                 destination_city, destination_airport_code,
                 out_date, return_date, stop_overs=0, via_city=""):
        self.price = price
        self.departure_airport_code = departure_airport_code
        self.departure_city = departure_city
        self.departure_city_code = departure_city_code
        self.destination_city = destination_city
        self.destination_city_code = destination_city_code
        self.destination_airport_code = destination_airport_code
        self.out_date = out_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city = via_city
