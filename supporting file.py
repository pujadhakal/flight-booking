from abc import ABC, abstractmethod
import csv


class Source(ABC):
    def get_headers(self):
        return [
            "Airlines Name",
            "Departure Time",
            "Arrival Time",
            "Departure Location",
            "Arrival Destination",
            "Flight Duration",
            "Direct FLight",
            "Layover Time",
            "Transit Location",
            "Transit Airport",
            "Price",
            "Source Link",
            "Scraped Website",
        ]

    @abstractmethod
    def scrape(self):
        raise NotImplementedError("Hello")

    def save_file(self, write_method="w"):
        with open("flight.csv", write_method, newline="") as file:
            writer = csv.writer(file)
            header = self.get_headers()
            data = self.scrape()
            if write_method == "w":
                writer.writerow(header)
            for entry in data:
                writer.writerow(
                    [
                        entry.airline_names,
                        entry.departure_time,
                        entry.arrival_time,
                        entry.departure_location,
                        entry.arrival_destination,
                        entry.flight_duration,
                        entry.direct_flight,
                        entry.layover_time,
                        entry.transit_location,
                        entry.transit_airport,
                        entry.flight_price,
                        entry.source,
                        entry.scraped_website,
                    ]
                )
