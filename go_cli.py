import sys
import requests
from argparse import ArgumentParser
import json

import go_api
import go_train
import go_bus

sys.path.insert(1, './') 
import trip
import line
import stop

NEW_LINE = "\n"
NEXT_SERVICE = "NextService"
LINES = "Lines"


# Parse the command line arguments
def get_arguments():

    parser = ArgumentParser()

    parser.add_argument("-k", "--key", dest="key", default="",
                        help="Your API key")
    
    parser.add_argument("-f", "--keyFile", dest="key_file", default="",
                        help="The file containing your API key")

    parser.add_argument("-s", "--stop", dest="stop", default="",
                        help="The stop you're interested in")
    
    parser.add_argument("-d", "--direction", dest="direction", default="",
                        help="The direction you want to go")
    
    parser.add_argument("-v", "--vehicle", dest="vehicle", default="",
                        help="The vehicle you're interested in")

    parser.add_argument("-c", "--config", action="store_true", default=False,
                        help="Dump the configuration")
    
    args = parser.parse_args()

    return args

args = get_arguments()
key = args.key

# -----------------------------------------------------------------------------
# 
# Example:
#
#  {
#     'StopCode': 'AP', 
#     'LineCode': 'LW', 
#     'LineName': 'Lakeshore West', 
#     'ServiceType': 'T',               # SERVICE_TRAIN
#     'DirectionCode': 'LW   ',         # 'LW' Westbound, 'LW   ' Eastbound!
#     'DirectionName': 'LW - West Harbour GO', 
#     'ScheduledDepartureTime': '2024-09-22 20:22:00', 
#     'ComputedDepartureTime': '2024-09-22 20:22:00', 
#     'DepartureStatus': 'E', 
#     'ScheduledPlatform': '1', 
#     'ActualPlatform': '', 
#     'TripOrder': 1, 
#     'TripNumber': '1731', 
#     'UpdateTime': '2024-09-22 20:19:45', 
#     'Status': 'M', 
#     'Latitude': 43.388724, 
#     'Longitude': -79.751464
#   }, 
# -----------------------------------------------------------------------------
def parse_response(json_trips):
    for tripFields in json_trips[NEXT_SERVICE][LINES]:
        this_trip = trip.Trip()
        this_trip.stop_code = tripFields[stop.CODE]
        this_trip.line.code = tripFields[line.CODE]
        this_trip.line.name = tripFields[line.NAME]
        this_trip.service_type = tripFields[trip.SERVICE_TYPE]
        this_trip.direction_code = tripFields[trip.DIRECTION_CODE]
        this_trip.direction_name = tripFields[trip.DIRECTION_NAME]

        scheduled_date_time = tripFields[trip.SCHEDULED_DEPARTURE_TIME]
        scheduled_date = scheduled_date_time.split(" ")[0]
        scheduled_time = scheduled_date_time.split(" ")[1][:5]
        this_trip.scheduled_departure_date = scheduled_date
        this_trip.scheduled_departure_time = scheduled_time

        computed_date_time = tripFields[trip.SCHEDULED_DEPARTURE_TIME]
        computed_date = computed_date_time.split(" ")[0]
        computed_time = computed_date_time.split(" ")[1][:5]
        this_trip.computed_departure_date = computed_date
        this_trip.computed_departure_time = computed_time

        this_trip.scheduled_platform = tripFields[trip.SCHEDULED_PLATFORM]
        this_trip.actual_platform = tripFields[trip.ACTUAL_PLATFORM]
        this_trip.order = tripFields[trip.TRIP_ORDER]
        this_trip.number = tripFields[trip.TRIP_NUMBER]
        this_trip.update_time = tripFields[trip.UPDATE_TIME]
        this_trip.status = tripFields[trip.STATUS]
        this_trip.latitude = tripFields[trip.LATITUDE]
        this_trip.longitude = tripFields[trip.LONGITUDE]

        print(this_trip.concise_str() + NEW_LINE)

if args.config:
    print(go_train.Lines)
    print(go_bus.Stops)

if args.stop:
    stop_code = args.stop

    api_url = go_api.GO_API_NEXT_SERVICE + str(stop_code) + go_api.KEY_FIELD + str(key)
    response = requests.get(api_url)

    # if request was successful
    if response.status_code == go_api.OK:
        # parse JSON response
        data = response.json()
        # do something with the data
        parse_response(data)
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
