"""A place, mostly the address portion of a stop."""

import sys

sys.path.insert(1, './') 
import facility
import parking

class Location:
    """A stop location parsed from the stop details endpoint.

    Example source endpoint:
        https://api.openmetrolinx.com/OpenDataAPI/api/V1/Stop/Details/AP

    Example payloads often omit unrelated fields and abbreviated facility or
    parking collections for brevity.
    """

    def __init__(self):
        self.street_number = "" # e.g. "5111"
        self.street_name = ""   # e.g. "Appleby Line"
        self.city = ""          # e.g. "Burlington"
        self.intersection = ""  # e.g. "Fairview Street and Appleby Line"
        self.zone_code = 0      # e.g. "15"
        self.longitude = 0      # e.g. -79.760991
        self.latitude = 0       # e.g. 43.379429
        self.driving_directions = "" # e.g. "Exit QEW @ Appleby Line; south..."
        self.driving_directions_fr = "" # French version
        self.facilities = []    # collection of Facility objects
        self.parking = []       # collection of Parking lots 
        self.type = ""

    STREET_NUMBER = "StreetNumber"  
    INTERSECTION = "Intersection"
    ZONE_CODE = "ZoneCode"
    LATITUDE = "Latitude"
    LONGITUDE = "Longitude"
    DRIVING_DIRECTIONS = "DrivingDirections"
    DRIVING_DIRECTIONS_FR = "DrivingDirectionsFr"
    FACILITIES = "Facilities"
    PARKING = "Parkings"

    def parse(self, json):
        self.street_number = json[self.STREET_NUMBER]
        self.latitude = json[self.LATITUDE]
        self.longitude = json[self.LONGITUDE]
        self.zone_code = json[self.ZONE_CODE]

        for facility_json in json[self.FACILITIES]:
            the_facility = facility.Facility()
            the_facility.parse_response(facility_json)
            self.facilities.append(the_facility)

        for parking_json in json[self.PARKING]:
            the_parking = parking.Parking()
            the_facility.parse_response(parking_json)
            self.parking.append(the_parking)

    def __str__(self):
        NEW_LINE = "\n"
        output = "street_number: " + self.street_number + NEW_LINE
        output += "latitude: " + str(self.latitude) + NEW_LINE
        output += "longitude: " + str(self.longitude) + NEW_LINE
        output += "type: " + self.type + NEW_LINE
        return output