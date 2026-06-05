"""A vehicle."""

import sys

sys.path.insert(1, './') 
import go_api

NEW_LINE = "\n"

class Vehicle:
    def __init__(self):
        self.id = ""            # e.g. "20241005-18-18050"
        self.is_deleted = False
        self.trip_update = "" # type of service e.g. SERVICE_TRAIN

    def __str__(self):
        output = "id: " + self.id + NEW_LINE
        output += "is_deleted: " + str(self.is_deleted) + NEW_LINE
        output += "trip_update: " + self.trip_update + NEW_LINE
        return output
    
    def parse_response(self, json_vehicle_position):
        """Parse a vehicle-position feed response.

        The feed may contain vehicle entries with statuses such as
        `INCOMING_AT` and `IN_TRANSIT_TO`.

        Example:
            {
                "header": {
                    "gtfs_realtime_version": "1.0",
                    "incrementality": "FULL_DATASET",
                    "timestamp": 1728119603
                },
                "entity": [
                    {
                        "id": "20241005-18-18050",
                        "is_deleted": false,
                        "trip_update": null,
                        "vehicle": {
                            "trip": {
                                "trip_id": "20241005-18-18050",
                                "route_id": "08241224-18",
                                "direction_id": 0,
                                "start_time": "04:30:00",
                                "start_date": "20241005",
                                "schedule_relationship": "SCHEDULED"
                            },
                            "vehicle": {
                                "id": "8560",
                                "label": "18B - Union Station",
                                "license_plate": ""
                            },
                            "position": {
                                "latitude": 43.45622,
                                "longitude": -79.68217,
                                "bearing": 0.0,
                                "odometer": 0.0,
                                "speed": 0.0
                            },
                            "stop_id": "00181",
                            "current_status": "IN_TRANSIT_TO",
                            "timestamp": 1728119585,
                            "congestion_level": "UNKNOWN_CONGESTION_LEVEL",
                            "occupancy_status": "EMPTY"
                        },
                        "alert": null
                    },
                    {
                        "id": "20241005-18-18060",
                        "...": "..."
                    }
                ]
            }
        """

        return True

    def get(self, key):
        
        api_url = f"{go_api.GO_API_VEHICLE_POSITION}{self.stop_code}{go_api.KEY_FIELD}{key}"
        response = requests.get(api_url)

        # if request was successful
        if response.status_code == go_api.OK:
            # parse JSON response
            data = response.json()
            # do something with the data
            self.parse_response(data)
        else:
            print("Failed to retrieve data. Status code:", response.status_code)

    def parse_stops_response(self, json):
        """Parse a trip-stop response.

        The expected payload is a stop list for a trip. Some portions of the
        API response may be omitted in examples for brevity.
        """
        
        json_trips = json[self.TRIPS][0]
        
        self.destination = json_trips[self.DESTINATION]            
        self.timestamp = json_trips[self.TIMESTAMP]
        self.status = json_trips[self.STATUS]
        self.latitude = json_trips[self.LATITUDE]
        self.longitude = json_trips[self.LONGITUDE]
        
        for tripFields in json_trips[self.STOPS]:

            this_stop = trip_stop.TripStop()

            this_stop.scheduled_arrival_time = tripFields[self.ARRIVAL_TIME][self.SCHEDULED]
            try:
                this_stop.computed_arrival_time = tripFields[self.ARRIVAL_TIME][self.COMPUTED]
            except:
                pass
            this_stop.scheduled_departure_time = tripFields[self.DEPARTURE_TIME][self.SCHEDULED]
            try:
                this_stop.computed_departure_time = tripFields[self.DEPARTURE_TIME][self.COMPUTED]
            except:
                pass
            this_stop.code = tripFields[this_stop.CODE]
            this_stop.status = tripFields[self.STATUS]
            this_stop.scheduled_track = tripFields[self.TRACK][self.SCHEDULED]
            this_stop.actual_track = tripFields[self.TRACK][self.ACTUAL]
            print(str(this_stop) + NEW_LINE)

    def get_stops(self, key, the_date=""):
        """Retrieve stops for this trip and parse them into this object.

        Args:
            key: The GO API key.
            the_date: Specific date for this trip in `YYYYMMDD` format.
        """

        # if no date provided, use today's date
        if not the_date:
            today = datetime.today()
            the_date = today.strftime('%Y%m%d')
        
        api_url = go_api.GO_API_SCHEDULE_TRIP + the_date + "/" + str(self.number) + go_api.KEY_FIELD + str(key)
        print(api_url)
        response = requests.get(api_url)

        # if request was successful
        if response.status_code == go_api.OK:
            # parse JSON response
            data = response.json()
            error_code = data[go_api.METADATA][go_api.ERROR_CODE]
            if int(error_code) == go_api.OK:
                # do something with the data
                self.parse_stops_response(data)
            else:
                print("Failed to retrieve data. Status code: " + error_code + ", message: " + data[go_api.METADATA][go_api.ERROR_MESSAGE])
        else:
            print("Failed to retrieve data. Status code:", response.status_code)

