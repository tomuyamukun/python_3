class FlightData:

    def __init__(
            self,
            price,
            origin_city,
            origin_airport,
            destination_city,
            destination_airport,
            out_data,
            return_data):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_data = out_data,
        self.return_data = return_data
