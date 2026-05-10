class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, departure, arrival, from_time, to_time):
        self.lowest_price = price
        self.departure = departure
        self.arrival = arrival
        self.from_time = from_time
        self.to_time = to_time
