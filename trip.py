import sys

sys.path.insert(1, './') 
import line

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

NEW_LINE = "\n"

class Trip:
    def __init__(self):
        self.number = 0
        self.order = 0
        self.service_type = "" # type of service e.g. SERVICE_TRAIN 
        self.line = line.Line()  # the line it's on
        self.stop_code = ""
        self.direction_code = ""
        self.direction_name = ""
        self.scheduled_departure_date = ""
        self.scheduled_departure_time = ""
        self.computed_departure_date = ""
        self.computed_departure_time = ""
        self.scheduled_platform = ""
        self.actual_platform = ""
        self.update_time = ""
        self.status = ""
        self.latitude = 0.0
        self.longitude = 0.0

    def __str__(self):
        output = "number: " + str(self.number) + NEW_LINE
        output += "order: " + str(self.order) + NEW_LINE
        output += "service_type: " + self.service_type + NEW_LINE
        output += "line_code: " + self.line.code + NEW_LINE
        output += "line: " + self.line.name + NEW_LINE
        output += "stop: " + self.stop_code + NEW_LINE
        output += "direction_code: " + self.direction_code + NEW_LINE
        output += "direction_name: " + self.direction_name + NEW_LINE
        output += "scheduled_departure_time: " + self.scheduled_departure_time + NEW_LINE
        output += "computed_departure_time: " + self.computed_departure_time + NEW_LINE
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