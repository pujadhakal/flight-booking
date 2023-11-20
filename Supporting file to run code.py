from dataclasses import dataclass
from typing import Optional


@dataclass
class FlightInformation:
    airline_names: Optional[str]
    departure_time: Optional[str]
    arrival_time: Optional[str]
    departure_location: Optional[str]
    arrival_destination: Optional[str]
    flight_duration: Optional[str]
    direct_flight: Optional[bool]
    layover_time: Optional[str]
    transit_location: Optional[str]
    transit_airport: Optional[str]
    flight_price: Optional[str]
    source: Optional[str]
    scraped_website: Optional[str]
