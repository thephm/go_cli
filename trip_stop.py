import sys
import requests
from datetime import datetime

sys.path.insert(1, './') 
import line
import stop
import go_api

NEW_LINE = "\n"

class TripStop(stop.Stop):
    def __init__(self):
        super(TripStop, self).__init__()
        self.number = ""
        self.order = ""
        self.code = ""
        self.direction_code = ""
        self.direction_name = ""
        self.scheduled_departure_date = ""
        self.scheduled_departure_time = ""
        self.computed_departure_date = ""
        self.computed_departure_time = ""
        self.scheduled_track = ""
        self.actual_track = ""
        self.scheduled_platform = ""
        self.actual_platform = ""
        self.update_time = ""
        self.status = ""
        self.latitude = 0.0
        self.longitude = 0.0
        
    SERVICE_TYPE = "ServiceType"
    DIRECTION_CODE = "DirectionCode"
    DIRECTION_NAME = "DirectionName"
    SCHEDULED_DEPARTURE_TIME = "ScheduledDepartureTime"
    COMPUTED_DEPARTURE_TIME = "ComputedDepartureTime"
    DEPARTURE_STATUS = "DepartureStatus"
    SCHEDULED_PLATFORM = "ScheduledPlatform"
    ACTUAL_PLATFORM = "ActualPlatform"
    TRIP_ORDER = "TripOrder"
    TRIP_NUMBER = "TripNumber"
    UPDATE_TIME = "UpdateTime"
    STATUS = "Status"
    LATITUDE = "Latitude"
    LONGITUDE = "Longitude"
    NEXT_SERVICE = "NextService"
    LINES = "Lines"
    TRIPS = "Trips"
    STOPS = "Stops"
    CODE = "Code"

    def __str__(self):
        output = super(TripStop, self).__str__()
        output += "number: " + str(self.number) + NEW_LINE
        output += "order: " + str(self.order) + NEW_LINE
        output += "service_type: " + self.service_type + NEW_LINE
        output += "line_code: " + self.line.code + NEW_LINE
        output += "line: " + self.line.name + NEW_LINE
        output += "code: " + self.code + NEW_LINE
        output += "direction_code: " + self.direction_code + NEW_LINE
        output += "direction_name: " + self.direction_name + NEW_LINE
        output += "scheduled_departure_time: " + self.scheduled_departure_time + NEW_LINE
        output += "computed_departure_time: " + self.computed_departure_time + NEW_LINE
        output += "scheduled_track: " +  str(self.scheduled_track) + NEW_LINE
        output += "actual_track: " +  str(self.actual_track) + NEW_LINE
        output += "scheduled_platform: " + self.scheduled_platform + NEW_LINE
        output += "actual_platform: " + self.actual_platform + NEW_LINE
        output += "update_time: " + self.update_time + NEW_LINE
        output += "status: " + self.status + NEW_LINE
        output += "latitude: " + str(self.latitude) + NEW_LINE
        output += "longitude: " +  str(self.longitude) + NEW_LINE
        return output
    
    def concise_str(self):
        output = ""
        if self.computed_departure_time:
            output += self.computed_departure_time
        else: 
            output += self.scheduled_departure_time

        output += " " + self.direction_name

        output += " on platform "
        if self.actual_platform:
            output += self.actual_platform
        else:
            output += self.scheduled_platform

        output += NEW_LINE + "trip: " + str(self.number) 
        output +=  NEW_LINE + "status: " + self.status
        if self.latitude != -1.0:
            output += NEW_LINE + "location: " + str(self.latitude) + ", " + str(self.longitude)
        return output
    
    def parse_response(self, json_trips):
        """Populate this trip stop from a NextService API response.

        Example:
            {
                'StopCode': 'AP',
                'LineCode': 'LW',
                'LineName': 'Lakeshore West',
                'ServiceType': 'T',
                'DirectionCode': 'LW   ',
                'DirectionName': 'LW - West Harbour GO',
                'ScheduledDepartureTime': '2024-09-22 20:22:00',
                'ComputedDepartureTime': '2024-09-22 20:22:00',
                'DepartureStatus': 'E',
                'ScheduledPlatform': '1',
                'ActualPlatform': '',
                'TripOrder': 1,
                'TripNumber': '1731',
                'UpdateTime': '2024-09-22 20:19:45',
                'Status': 'M',
                'Latitude': 43.388724,
                'Longitude': -79.751464,
            }
        """
        for tripFields in json_trips[self.NEXT_SERVICE][self.LINES]:
            self.destination = tripFields[self.DESTINATION]
            self.line.code = tripFields[line.CODE]
            self.line.name = tripFields[line.NAME]
            self.service_type = tripFields[self.SERVICE_TYPE]
            self.direction_code = tripFields[self.DIRECTION_CODE]
            self.direction_name = tripFields[self.DIRECTION_NAME]

            scheduled_date_time = tripFields[self.SCHEDULED_DEPARTURE_TIME]
            scheduled_date = scheduled_date_time.split(" ")[0]
            scheduled_time = scheduled_date_time.split(" ")[1][:5]
            self.scheduled_departure_date = scheduled_date
            self.scheduled_departure_time = scheduled_time

            computed_date_time = tripFields[self.SCHEDULED_DEPARTURE_TIME]
            computed_date = computed_date_time.split(" ")[0]
            computed_time = computed_date_time.split(" ")[1][:5]
            self.computed_departure_date = computed_date
            self.computed_departure_time = computed_time

            self.scheduled_platform = tripFields[self.SCHEDULED_PLATFORM]
            self.actual_platform = tripFields[self.ACTUAL_PLATFORM]
            self.order = tripFields[self.TRIP_ORDER]
            self.number = tripFields[self.TRIP_NUMBER]
            self.update_time = tripFields[self.UPDATE_TIME]
            self.status = tripFields[self.STATUS]
            self.latitude = tripFields[self.LATITUDE]
            self.longitude = tripFields[self.LONGITUDE]

            print(self.concise_str() + NEW_LINE)

    def next_service(self, key):
        """Fetch the next service for the current stop using the GO Transit API.

        Args:
            key (str): The GO API key for authentication.
        """
        
        api_url = f"{go_api.GO_API_NEXT_SERVICE}{self.stop_code}{go_api.KEY_FIELD}{key}"
        response = requests.get(api_url)

        if response.status_code == go_api.OK:
            data = response.json()
            self.parse_response(data)
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
