class FlightData:

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

def find_cheapest_flight(data, return_date):
    # Handle empty data if no flight data is returned
    if data is None or (not data.get("best_flights") and not data.get("other_flights")):
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    # Combine best_flights and other_flights into one list
    all_flights = data.get("best_flights", []) + data.get("other_flights", [])

    # Data from the first flight in the list
    first_flight = all_flights[0]
    lowest_price = first_flight["price"]
    origin = first_flight["flights"][0]["departure_airport"]["id"]
    destination = first_flight["flights"][-1]["arrival_airport"]["id"]
    out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]

    # Initialize FlightData with the first flight for comparison
    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

    for flight in all_flights:
        # Exception handling - json has data but flight is missing 'price'. Skip.
        try:
            price = flight["price"]
        except KeyError:
            print("--- No price available for flight. ---")
            continue
        if price < lowest_price:
            lowest_price = price
            origin = flight["flights"][0]["departure_airport"]["id"]
            destination = flight["flights"][-1]["arrival_airport"]["id"]
            out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
            print(f"Lowest price to {destination} is GBP {lowest_price}")

    return cheapest_flight
