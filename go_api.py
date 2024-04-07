# -----------------------------------------------------------------------------
#
# Constant strings for the endpoints of the GO API.
#
# This is unofficial and unsupported, copied from here as at 2024-04-06:
#
# http://api.openmetrolinx.com/OpenDataAPI/Help/Index/en 
# 
# Do not contact anyone at Metrolinx or GO Transit with questions on this file.
#
# All of the endpoints are for reading (GET), none for updating.
#
# -----------------------------------------------------------------------------

GO_API_BASE = "http://api.openmetrolinx.com/OpenDataAPI/api/V1/"

KEY_FIELD = "?key="

# Endpoints
TRIP = "Trip"
STOP = "Stop"
SCHEDULE = "Schedule"

LINE = "Line"

TRAIN = "Train"
TRAINS = "Trains"
BUS = "Bus"

ALL = "All"

FARES = "Fares"
ALERTS = "Alerts"
TRIP_UPDATES = "TripUpdates"
EXCEPTIONS = "Exceptions"
VEHICLE_POSITION = "VehiclePosition"
SERVICEUPDATE = "ServiceUpdate"

# Return codes
OK = 200           # No error
NO_CONTENT = 204   # No data was found
BAD_REQUEST = 400  # server cannot process the request due to a malformed client request.
UNAUTHORIZED = 401 # key was missing or incorrect.
FORBIDDEN = 403    # key does not have access to the topic.
NOT_FOUND = 404    # URI is invalid or the resource does not exist.
GONE = 410         # API version no longer exists. Use the current version.
TOO_MANY_REQUESTS = 429 # key's use limit has been reached
INTERNAL_ERROR = 500 # Internal Server Error. There is an issue. Please post on the developers forums so the issue can be resolved.
UNAVAILABLE = 503  # Open data servers are down or overloaded with requests. Try again later.
TIMEOUT = 504      # A server did not respond. Try again later.

# Service Types
SERVICE_TYPE_TRAIN = "T"
SERVICE_TYPE_BUS = "B"

# ScheduleJourney uses these (and "B")
SERVICE_TYPE_RAIL = "R"
SERVICE_TYPE_RAIL_AND_BUS = "RB"

# Service Code used in ScheduleJourney
# e.g. "01"

# Accessible in ScheduleJourney - Services
JOURNEY_ACCESSIBLE_RAIL = "R"
JOURNEY_ACCESSIBLE_BUS = "B"
JOURNEY_ACCESSIBLE_RAIL_AND_BUS = "RB"

# Delay Status
DELAY_STATUS_STOPPED = "S"
DELAY_STATUS_MOVING = "M"

# Departure Status
DEPARTURE_STATUS_ESTIMATED = "E"
DEPARTURE_STATUS_CANCELLED = "C"
DEPARTURE_STATUS_ACTUAL = "A"

# Station Facilities
FACILITY_CODE_ABM = "ABM"   # Automatic bank teller machine
FACILITY_CODE_BR  = "BR"    # Bicycle rack
FACILITY_CODE_DCA = "DCA"   # Debit cards accepted 
FACILITY_CODE_EV = "EV"     # Elevators
FACILITY_CODE_NEWS = "NEWS" # Newspaper box
FACILITY_CODE_PP = "PP"     # Pay phones
FACILITY_CODE_PW = "PW"     # Public washroom
FACILITY_CODE_SB = "SB"     # Station building
FACILITY_CODE_TAXI = "TAXI" # Taxi stand
FACILITY_CODE_TVM = "TVM"   # Ticket vending machine
FACILITY_CODE_RK = "RK"     # Refreshment kiosk
FACILITY_CODE_WR = "WR"     # Waiting room
FACILITY_CODE_WAT = "WAT"   # Wheelchair accessible train service

# Station Facilities > Parking
PARKING_REGULAR = "Regular"
PARKING_STRUCTURE = "Structure"

# Indicates if the stop is Major (true) or not (false). 
# 
# Major Stop is the location that serves as a transfer point between a large
# number of route. Minor Stop is the location where the bus stop for a short 
# period of time to drop off or pick up passengers.
IS_MAJOR_STOP = 1
IS_NOT_MAJOR_STOP = 0 # Minor stop

# Location type descriptions in "Stop" 
BUS_STOP = "Bus Stop"
BUS_TERMINAL = "Bus Terminal"
CARPOOL_LOT = "Carpool Lot"
GO_TERMINAL = "GO Terminal"
PARK_AND_RIDE = "Park & Ride"
GO_PARK_AND_RIDE = "GO Park & Ride"
TRAIN_STATION = "Train Station"
TICKET_AGENCY = "Ticket Agency"
TRAIN_AND_BUS_STATION = "Train & Bus Station"
TICKET_AGENCY_AND_STOP = "Ticket Agency & Stop"
TICKET_AGENCY_AND_TERMINAL = "Ticket Agency & Terminal"

# Location types (not returned, here for reference)
BUS_STOP_CODE = "BS"
BUS_TERMINAL_CODE = "BT"
CARPOOL_LOT_CODE = "CL"
GO_TERMINAL_CODE = "GT"
PARK_AND_RIDE_CODE = "PK"
GO_PARK_AND_RIDE_CODE = "PR"
TRAIN_STATION_CODE = "ST"
TICKET_AGENCY_CODE = "TA"
TRAIN_AND_BUS_STATION_CODE = "TB"
TICKET_AGENCY_AND_STOP_CODE = "TS"
TICKET_AGENCY_AND_TERMINAL_CODE = "TT"

# Service Alerts
DISRUPTION = "Service Disruption"
DISRUPTION_SUSPENSION = "Train Service Suspension"

SERVICE_ALERT_INIT = "INIT" # Initial
SERVICE_ALERT_CORR = "CORR" # Corrected
SERVICE_ALERT_FINAL = "FINAL" # Final
SERVICE_ALERT_UPD = "UPD" # Updated

# Line Codes used in ServiceAlertAll
LINE_CODE_LAKESHORE_WEST = "LW"
LINE_CODE_LAKESHORE_EAST = "LE"
LINE_CODE_KITCHENER = "GT"
LINE_CODE_STOUFVILLE = "ST"
LINE_CODE_RICHMOND_HILL = "RH"
LINE_CODE_BARRIE = "BI"
LINE_CODE_MILTON = "MI"

# Line colours used in ScheduleJourney
LINE_COLOUR_LAKESHORE_EAST = "#FF0D00"
LINE_COLOUR_LAKESHORE_WEST = "#98002E"
LINE_COLOUR_BARRIE = "#003767"
LINE_COLOUR_MILTON = "#F57F25"
LINE_COLOUR_KITCHENER = "#00853E"
LINE_COLOUR_STOUFVILLE = "#794500"
LINE_COLOUR_RICHMOND_HILL = "#0099C7"

# Stop Codes
UNION = "UN"
TBD = "SR"
TBD2 = "ME"
TBD3 = "BO"
STOP_CODE_TBD = "00139" 
STOP_CODE_TBD1 = "02408"
STOP_CODE_TBD2 = "02646"
STOP_CODE_TBD3 = "02404"

# https://www.gotransit.com/en/find-a-station-or-stop/ex/station-details

# Lakeshore West Line
EXHIBITION_GO = "EX"   # https://www.gotransit.com/en/find-a-station-or-stop/ex
MIMICO_GO = "MI"       # https://www.gotransit.com/en/find-a-station-or-stop/mi
LONG_BRANCH_GO = "LO"  # https://www.gotransit.com/en/find-a-station-or-stop/lo
PORT_CREDIT_GO = "PO"  # https://www.gotransit.com/en/find-a-station-or-stop/po
CLARKSON_GO = "CL"     # https://www.gotransit.com/en/find-a-station-or-stop/cl
OAKVILLE_GO = "OA"     # https://www.gotransit.com/en/find-a-station-or-stop/oa
BRONTE_GO = "BO"       # https://www.gotransit.com/en/find-a-station-or-stop/bo
APPLEBY_GO = "AP"      # https://www.gotransit.com/en/find-a-station-or-stop/ap
BURLINGTON_GO = "BU"   # https://www.gotransit.com/en/find-a-station-or-stop/bu
ALDERSHOT_GO = "AL"    # https://www.gotransit.com/en/find-a-station-or-stop/al
HAMILTON_GO = "HA"     # https://www.gotransit.com/en/find-a-station-or-stop/ha
WEST_HARBOUR_GO = "WR" # https://www.gotransit.com/en/find-a-station-or-stop/wr
ST_CATHARINES_GO = "SCTH" # https://www.gotransit.com/en/find-a-station-or-stop/scth - Via
NIAGARA_FALLS_GO = "NI"   # https://www.gotransit.com/en/find-a-station-or-stop/ni - Via

# Lakeshore East Line

DANFORTH_GO = "DA"     # https://www.gotransit.com/en/find-a-station-or-stop/da
SCARBOROUGH_GO = "SC"  # https://www.gotransit.com/en/find-a-station-or-stop/sc
EGLINGTON_GO = "EG"    # https://www.gotransit.com/en/find-a-station-or-stop/eg
GUILDWOOD_GO = "GU"    # https://www.gotransit.com/en/find-a-station-or-stop/gu
ROUGE_HILL_GO = "RO"   # https://www.gotransit.com/en/find-a-station-or-stop/ro
PICKERING_GO = "PIN"   # https://www.gotransit.com/en/find-a-station-or-stop/pin
AJAX_GO = "AJ"         # https://www.gotransit.com/en/find-a-station-or-stop/aj
WHITBY_GO = "WH"       # https://www.gotransit.com/en/find-a-station-or-stop/wh
OSHAWA_GO = "OS"       # https://www.gotransit.com/en/find-a-station-or-stop/os Durham College Oshawa GO

UNION_STATION = "USTN" # https://www.gotransit.com/en/find-a-station-or-stop/un

# Barrie Line

DOWNSVIEW_GO = "DW"    # https://www.gotransit.com/en/find-a-station-or-stop/dw
RUTHERFORD_GO = "RU"   # https://www.gotransit.com/en/find-a-station-or-stop/ru
MAPLE_GO = "MP"        # https://www.gotransit.com/en/find-a-station-or-stop/mp
KING_CITY_GO = "KC"    # https://www.gotransit.com/en/find-a-station-or-stop/kc
AURORA_GO = "AU"       # https://www.gotransit.com/en/find-a-station-or-stop/au
NEWMARKET_GO = "NE"    # https://www.gotransit.com/en/find-a-station-or-stop/ne
EAST_GWILLIMBURY_GO = "EA" # https://www.gotransit.com/en/find-a-station-or-stop/ea
BRADFORD_GO = "BD"     # https://www.gotransit.com/en/find-a-station-or-stop/bd
BARRIE_SOUTH_GO = "BA" # https://www.gotransit.com/en/find-a-station-or-stop/ba
ALLANDALE_WATERFRONT_GO = "AD" # https://www.gotransit.com/en/find-a-station-or-stop/ad

# Kitchener Line has 11 Stops

BLOOR_GO = "BL"      # https://www.gotransit.com/en/find-a-station-or-stop/bl
WESTON_GO = "WE"     # https://www.gotransit.com/en/find-a-station-or-stop/we
ETOBICOKE_NORTH_GO = "ET" # https://www.gotransit.com/en/find-a-station-or-stop/et
MALTON_GO = "MA"     # https://www.gotransit.com/en/find-a-station-or-stop/ma
BRAMALEA_GO = "BE"   # https://www.gotransit.com/en/find-a-station-or-stop/be
BRAMPTON_GO = "BR"   # https://www.gotransit.com/en/find-a-station-or-stop/br Brampton Innovation District GO
MOUNT_PLEASANT_GO = "MO" # https://www.gotransit.com/en/find-a-station-or-stop/mo
GEORGETOWN_GO = "GE" # https://www.gotransit.com/en/find-a-station-or-stop/ge
ACTON_GO = "AC"      # https://www.gotransit.com/en/find-a-station-or-stop/ac
GUELPH_GO = "GL"     # https://www.gotransit.com/en/find-a-station-or-stop/gl Guelph Central GO
KITCHENER_GO = "KI"  # https://www.gotransit.com/en/find-a-station-or-stop/ki

# Milton Line

KIPLING_GO = "KP"      # https://www.gotransit.com/en/find-a-station-or-stop/kp
DIXIE_GO = "DI"        # https://www.gotransit.com/en/find-a-station-or-stop/di
COOKSVILLE_GO = "CO"   # https://www.gotransit.com/en/find-a-station-or-stop/co
ERINDALE_GO = "ER"     # https://www.gotransit.com/en/find-a-station-or-stop/er
STREETSVILLE_GO = "SR" # https://www.gotransit.com/en/find-a-station-or-stop/sr
MEADOWVALE_GO = "ME"   # https://www.gotransit.com/en/find-a-station-or-stop/me
LISGAR_GO = "LS"       # https://www.gotransit.com/en/find-a-station-or-stop/ls
MILTON_GO = "ML"       # https://www.gotransit.com/en/find-a-station-or-stop/ml

# Richmond Hill Line

ORIOLE_GO = "OR"        # https://www.gotransit.com/en/find-a-station-or-stop/or
OLD_CUMMER_GO = "OL"    # https://www.gotransit.com/en/find-a-station-or-stop/ol
LANGSTAFF_GO = "LA"     # https://www.gotransit.com/en/find-a-station-or-stop/la
RICHMOND_HILL_GO = "RI" # https://www.gotransit.com/en/find-a-station-or-stop/ri
GORMLEY_GO = "GO"       # https://www.gotransit.com/en/find-a-station-or-stop/go
BLOOMINGTON_GO = "BM"   # https://www.gotransit.com/en/find-a-station-or-stop/bm

# Stouffville Line

# DANFORTH_GO = "DA"
SCARBOROUGH_GO = "SC"  # https://www.gotransit.com/en/find-a-station-or-stop/sc
KENNEDY_GO = "KE"      # https://www.gotransit.com/en/find-a-station-or-stop/ke
AGINCOURT_GO = "AG"    # https://www.gotransit.com/en/find-a-station-or-stop/ag
MILLIKEN_GO = "MK"     # https://www.gotransit.com/en/find-a-station-or-stop/mk
UNIONVILLE_GO = "UI"   # https://www.gotransit.com/en/find-a-station-or-stop/ui
CENTENNIAL_GO = "CE"   # https://www.gotransit.com/en/find-a-station-or-stop/ce
MARKHAM_GO = "MR"      # https://www.gotransit.com/en/find-a-station-or-stop/mr
MOUNT_JOY_GO = "MJ"    # https://www.gotransit.com/en/find-a-station-or-stop/mj
STOUFFVILLE_GO = "ST"  # https://www.gotransit.com/en/find-a-station-or-stop/st
OLD_ELM_GO = "LI"      # https://www.gotransit.com/en/find-a-station-or-stop/li

# Flags in ExceptionsTrain
IS_CANCELLED = 1
IS_NOT_CANCELLED = 0
IS_OVERRIDE = 1
IS_NOT_OVERRIDE = 0
IS_STOPPING = 1
IS_NOT_STOPPING = 0

# Bus Types
BUS_TYPE_COACH = "Coach"

# LineCode
# The code representing the bus line/route.
# For example: 12 – this represents "Niagara Falls"
BUS_ROUTE_NIAGARA = 12

# Route Number
#
# Route Number 12B vs. Line Code 12.
# When the Route Number is the same as the Line Code, a normal route was taken.
# When the Route Number includes a letter this shows there was a change to the

# Directions
NORTH = "N"
SOUTH = "S"
WEST = "W"
EAST = "E"

# Line Direction
LINE_DIRECTION_NORTH = "N"
LINE_DIRECTION_SOUTH = "S"
LINE_DIRECTION_WEST = "W"
LINE_DIRECTION_EAST = "E"
LINE_DIRECTION_UNION_IN = "In"
LINE_DIRECTION_UNION_OUT = "Out"

# Motion
IN_MOTION = 0 # No, not moving
NOT_IN_MOTION = 1 # Yes, moving

# Number of cars
SIX_CARS = 6
TEN_CARS = 10
TWELVE_CARS = 12

# Fare Types
FARE_ADULT = "Adult"
FARE_STUDENT = "Student"
FARE_SENIOR = "Senior"
FARE_CHILD = "Child"
FARE_GROUP_PASS = "Group Pass"

# Fare Type Categories
FARE_SINGLE_RIDE_ADULT = "Single Ride Adult"
FARE_DAY_PASS_ADULT = "Day Pass Adult"
FARE_PRESTO_1_TO_35 = "PretoTrips1-35"
FARE_PRESTO_36_TO_40 = "PretoTrips36-40"
FARE_PRESTO_41_PLUS = "PretoTrips41+"

# Fare Categories
FARE_CATEGORY_NORMAL = "Normal"
FARE_CATEGORY_DISCOUNT = "Discount"

# GTFS
GTFS_CONGESTION_LEVEL_UNKNOWN = "Unknown Congestion"

# GTFS TripUpdate
GTFS_SCHEDULE_RELATIONSHIP_SCHEDULED = "Scheduled"
GTFS_SCHEDULE_RELATIONSHIP_ADDED = "Added"
GTFS_SCHEDULE_RELATIONSHIP_UNSCHEDULED = "Unscheduled"
GTFS_SCHEDULE_RELATIONSHIP_CANCELLED = "Cancelled"

# GTFS Alerts
GTFS_ALERT_UNKNOWN_CAUSE = "Unknown cause"
GTFS_ALERT_UNKNOWN_EFFECT = "Unknown effect"
GTFS_ENGLISH = "en"
GTFS_FRENCH = "fr"

# Ticket Type
TICKET_PAPER = "Paper"
TICKET_PRESTO = "Presto"

# -----------------------------------------------------------------------------
#
# Stop
#
# Returns information on Stops. 
#
# Every stop has a code called the "StopCode"
#
# Stops are locations where there is scheduled service and this returns 
# predictions for all lines for a set stop.
#
# Requests with "api/V1/Stop.xml" or "api/V1/Stop.json" or "api/V1/Stop" 
# displays data in xml and json format respectively.
#
# -----------------------------------------------------------------------------

GO_API_STOP = GO_API_BASE + STOP + "/"

# Displays predictions for all lines that feed a certain bus or train stop
# 
# Next Service is the lines (rail lines and bus routes) that feed the stop. 
# Returns: Bus or train lines / routes that feed the given stop
#
# api/V1/Stop/NextService/{StopCode}	
GO_API_NEXT_SERVICE = GO_API_STOP + "NextService/"

# No documentation available
# api/V1/Stop/Details/{StopCode}	
GO_API_STOP_DETAILS = GO_API_STOP + "Details/"

# Displays Destinations of a stop
# api/V1/Stop/Destinations/{StopCode}/{FromTime}/{ToTime}
GO_API_DESTINATIONS = GO_API_BASE + "Stop/Destinations/"

# api/V1/Stop/All	
GO_API_STOPS = GO_API_STOP + "/" + ALL

# -----------------------------------------------------------------------------
#
# Service Update
#
# Returns information on Alert messages, train or bus departures from Union and 
# Service Guarantee for the trip. Requests with "api/V1/ServiceUpdate.xml" or 
# "api/V1/ServiceUpdate.json" or "api/V1/ServiceUpdate" displays data in xml and 
# json format respectively.
#
# All endpoints use GET, start with "api/V1/ServiceUpdate/InformationAlert/All"
# 
# -----------------------------------------------------------------------------

GO_API_SERVICE_UPDATE =  GO_API_BASE + SERVICEUPDATE + "/"

# Service alert messages by date
# api/V1/ServiceUpdate/ServiceAlert/All
GO_API_SERVICE_ALERT = GO_API_SERVICE_UPDATE + "ServiceAlert/" + ALL

# Information alert messages by date
# api/V1/ServiceUpdate/InformationAlert/All
GO_API_INFORMATION_ALERT = GO_API_SERVICE_UPDATE + "InformationAlert/" + ALL

# Nearest departures for buses and trains from Union Station
# api/V1/ServiceUpdate/UnionDepartures/All	
GO_API_UNION_DEPARTURES = GO_API_SERVICE_UPDATE + "UnionDepartures/" + ALL

# Schedule exceptions
GO_API_EXCEPTIONS = GO_API_SERVICE_UPDATE + EXCEPTIONS + "/"

# Cancelled train trips/stops: api/V1/ServiceUpdate/Exceptions/Train	
GO_API_EXCEPTIONS_TRAIN = GO_API_EXCEPTIONS + TRAIN

# Cancelled bus trips/stops: api/V1/ServiceUpdate/Exceptions/Bus	
GO_API_EXCEPTIONS_BUS = GO_API_EXCEPTIONS + BUS

# All cancelled trips/stops: api/V1/ServiceUpdate/Exceptions/All	
GO_API_EXCEPTIONS_ALL = GO_API_EXCEPTIONS + ALL

# -----------------------------------------------------------------------------
#
# Service At Glance
#
# Returns information on service bus and train trips. 
# 
# Requests with "api/V1/ServiceataGlance.xml" or "api/V1/ServiceataGlance.json" 
# or "api/V1/ServiceataGlance" displays data in XML and JSON.
#
# All endpoints use GET, start with "api/V1/ServiceataGlance/" and the get
# all in service trips.
#
# -----------------------------------------------------------------------------

# Bus trips: api/V1/ServiceataGlance/Buses/All
GO_API_SERVICE_AT_A_GLANCE = GO_API_BASE + "ServiceataGlance/"

# Train trips: api/V1/ServiceataGlance/Trains/All
GO_API_SERVICE_AT_A_GLANCE_TRAINS = GO_API_SERVICE_AT_A_GLANCE + TRAINS + "/" + ALL

# -----------------------------------------------------------------------------
#
# Schedule
#
# Returns information on Schedules by Line, Schedules by Stop and Journey. 
# 
# Requests with "api/V1/Schedule.xml" or "api/V1/Schedule.json" or 
# "api/V1/Schedule" displays data in xml and json format respectively.
#
# -----------------------------------------------------------------------------

GO_API_SCHEDULE = GO_API_BASE + SCHEDULE + "/"

# A Journey’s lines (rail corridor and bus routes), trips, stops and transfers.
#
# api/V1/Schedule/Journey/{Date}/{FromStopCode}/{ToStopCode}/{StartTime}/{MaxJourney}	
#
# api/V1/Schedule/Journey/{Date}/{FromStopCode}/{StartTime}/{MaxJourney}?ToStopCode={ToStopCode}

GO_API_SCHEDULE_JOURNEY = GO_API_SCHEDULE + "Journey/"

# Line detail based on date, line code and direction
# api/V1/Schedule/Line/{Date}/{LineCode}/{LineDirection}	
GO_API_SCHEDULE_LINE = GO_API_SCHEDULE + LINE + "/"

# Lines in effect for the date provided
# api/V1/Schedule/Line/All/{Date}	
GO_API_SCHEDULE_LINE_ALL = GO_API_SCHEDULE_LINE + ALL + "/"

# Line stops in effect for the date, line code and line direction given.
# api/V1/Schedule/Line/Stop/{Date}/{LineCode}/{LineDirection}	
GO_API_SCHEDULE_STOP = GO_API_SCHEDULE_LINE + STOP + "/"

# Trip stops in effect for the given trip number and date
# api/V1/Schedule/Trip/{Date}/{TripNumber}	
GO_API_SCHEDULE_TRIP = GO_API_SCHEDULE_LINE + TRIP + "/"

# -----------------------------------------------------------------------------
#
# GTFS Feeds
#
# Returns GTFS real time feeds. Requests with "api/V1/Gtfs.xml" or 
# "api/V1/Gtfs.json" or "api/V1/Gtfs.proto" or "api/V1/Gtfs" displays data in 
# XML, JSON and protobuffer format respectively.
#
# Vehicle position - all live trips with trip number, start time, destination,
# current vehicle location in lat/long and stop ID, vehicle number.
#
# Trip updates - all live trips with trip number, direction, start time, 
# destination and info for each upcoming stop on the trip including stop ID, 
# scheduled arrival time in epoch, delay deivation, and if scheduled stop or
# added stop.
#
# Alerts - general service alerts, planned bus stop relocations and route 
# detours broken down by route/line, station construction and elevator status
# notices broken odwn by line and station.
#
# -----------------------------------------------------------------------------

GO_API_GTFS_FEED = GO_API_BASE + "Gtfs/Feed/"

# All alert feeds: api/V1/Gtfs/Feed/Alerts	
GO_API_ALERTS = GO_API_GTFS_FEED + ALERTS

# All trip update feeds: api/V1/Gtfs/Feed/TripUpdates	
GO_API_TRIP_UPDATES = GO_API_GTFS_FEED + TRIP_UPDATES

# All vehicle position feeds: api/V1/Gtfs/Feed/VehiclePosition	
GO_API_VEHICLE_POSITION = GO_API_GTFS_FEED + VEHICLE_POSITION

# -----------------------------------------------------------------------------
#
# Up Express Feed
#
# UPGTFSRealTimeV1
#
# Like "GET api/V1/UP/Gtfs/Feed/Alerts"
#
# -----------------------------------------------------------------------------

GO_API_UP_GTFS_FEED = GO_API_BASE + "UP/Gtfs/Feed/"

# api/V1/UP/Gtfs/Feed/Alerts
GO_API_UP_ALERTS = GO_API_UP_GTFS_FEED + ALERTS

# api/V1/UP/Gtfs/Feed/TripUpdates
GO_API_UP_TRIP_UPDATES = GO_API_UP_GTFS_FEED + TRIP_UPDATES

# api/V1/UP/Gtfs/Feed/VehiclePosition
GO_API_UP_VEHICLE_POSITION = GO_API_UP_GTFS_FEED + VEHICLE_POSITION

# -----------------------------------------------------------------------------
#
# Fleet
#
# Returns GTFS real time feeds with Occupancy percentage and Consist 
# information. Requests with "api/V1/Fleet.xml " or "api/V1/Fleet.json " 
# or "api/V1/Fleet.proto " display data in xml, json and protobuffer format
# respectively. The default return type is json for "api/V1/Fleet ".
#
# -----------------------------------------------------------------------------

GO_API_FLEET = GO_API_BASE + "Fleet/"

GO_API_FLEET_CONSIST = GO_API_FLEET + "Consist/"

# All consists data: api/V1/Fleet/Consist/All
GO_API_FLEET_CONSIST_ALL = GO_API_FLEET_CONSIST + ALL

# Returns consist for engine: api/V1/Fleet/Consist/Engine/{EngineNumber}	
GO_API_FLEET_CONSIST_ENGINE = GO_API_FLEET_CONSIST + "Engine/"

# -----------------------------------------------------------------------------
#
# Fleet Occupancy
#
# These endpoints start with "api/V1/Fleet/Occupancy/GtfsRT/Feed/"
#
# -----------------------------------------------------------------------------

GO_API_FLEET_OCCUPANCY = GO_API_FLEET + "Occupancy/GtfsRT/Feed"

# All alert feeds: api/V1/Fleet/Occupancy/GtfsRT/Feed/Alerts	
GO_API_FLEET_OCCUPANCY_ALERTS = GO_API_FLEET_OCCUPANCY + ALERTS

# All trip update feeds: api/V1/Fleet/Occupancy/GtfsRT/Feed/TripUpdates	
GO_API_FLEET_OCCUPANCY_TRIP_UPDATES = GO_API_FLEET_OCCUPANCY + TRIP_UPDATES

# All vehicle position feeds: api/V1/Fleet/Occupancy/GtfsRT/Feed/VehiclePosition	
GO_API_FLEET_OCCUPANCY_VEHICLE_POSITION = GO_API_FLEET_OCCUPANCY + VEHICLE_POSITION

# -----------------------------------------------------------------------------
#
# Fare
#
# Returns information on Fares between stations. Requests with "api/V1/Fares.xml" or "api/V1/Fares.json" or "api/V1/Fares" displays data in xml and json format respectively.
#
# -----------------------------------------------------------------------------

# All fares between two stations: api/V1/Fares/{FromStopCode}/{ToStopCode}	

# All fares between two stations for an operational day:
# api/V1/Fares/{FromStopCode}/{ToStopCode}/{OperationalDay}	

GO_API_FARES = GO_API_BASE + FARES + "/"
