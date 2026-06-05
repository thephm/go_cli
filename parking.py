"""Parking data returned by the stop details endpoint.

Example source endpoint:
    https://api.openmetrolinx.com/OpenDataAPI/api/V1/Stop/Details/AP

Examples usually omit response fields unrelated to parking.
"""
    
class Parking:
    def __init__(self):
        self.name = ""      # e.g. "North Lot"
        self.name_fr = ""   # French version of `name``
        self.spots = 0      # Number of parking spots
        self.type = ""      # e.g. "Main Lot"

    NAME = "Name"
    NAME_FR = "NameFr"
    SPOTS = "ParkSpots"
    TYPE = "Type"
    
    def parse(self, json_parking):
        try:
            self.name = json_parking[self.NAME]
            self.name_fr = json_parking[self.NAME_FR]
            self.spots = json_parking[self.SPOTS]
            self.type = json_parking[self.TYPE]
        except:
            pass

    def __str__(self):
        NEW_LINE = "\n"
        output = "name: " + self.name + NEW_LINE
        output += "name_fr: " + self.name_fr + NEW_LINE
        output += "spots: " + str(self.spots) + NEW_LINE
        output += "type: " + self.type + NEW_LINE