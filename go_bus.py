# Service Types
SERVICE_BUS = "B"

# Bus Types
BUS_TYPE_COACH = "Coach"

# Location type descriptions in "Stop" 
BUS_STOP = "Bus Stop"
BUS_TERMINAL = "Bus Terminal"
CARPOOL_LOT = "Carpool Lot"
PARK_AND_RIDE = "Park & Ride"
TRAIN_AND_BUS_STATION = "Train & Bus Station"

# LineCode
# The code representing the bus line/route.
# For example: 12 � this represents "Niagara Falls"
NiagaraBusRoute = {
    "number": 12,
    "stops": []
}

# Route Number
#
# Route Number 12B vs. Line Code 12.
# When the Route Number is the same as the Line Code, a normal route was taken.
# When the Route Number includes a letter this shows there was a change to the

# -----------------------------------------------------------------------------
# Stop Codes
# 
# Unique label for each train station.
#
# -----------------------------------------------------------------------------

# Union 
UNION_STATION_BUS_TERMINAL = "USTN"

union_station_bus_terminal = usbt = { 
    "code": UNION_STATION_BUS_TERMINAL,
    "type": BUS_TERMINAL,
    "service": SERVICE_BUS,
    "lat": "",
    "long": "",
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/un"
}

# -----------------------------------------------------------------------------
#
# Bus Stop Codes
# 
# Unique label for each train station.
#
# -----------------------------------------------------------------------------

Dundas407 = {
    "code": "00139",
    "type": BUS_STOP,
    "route": "",
    "name": "Dundas St. @ Hwy. 407 Park & Ride",
    "address": "Northampton Boulevard, Burlington",
    "lat": "",
    "long": "",
    "service": SERVICE_BUS,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/00139/station-details"
}

NiagaraFallsBus = {
    "code": "02408",
    "type": BUS_TERMINAL,
    "route": "",
    "name": "Niagara Falls Bus Terminal",
    "address": "4555 Erie Avenue, Niagara Falls, ON",
    "lat": "",
    "long": "",
    "service": SERVICE_BUS,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/02408/station-details"
}

NiagaraCollege = {
    "code": "02646",
    "type": BUS_STOP,
    "route": "",
    "name": "Niagara College",
    "address": "135 Taylor Road, Niagara-on-the-Lake, ON",
    "lat": "",
    "long": "",
    "service": SERVICE_BUS,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/02646/station-details"
}

Stanley420 = {
    "code": "02404",
    "type": PARK_AND_RIDE,
    "route": "",
    "name": "Stanley Ave. @ Hwy. 420 Park & Ride",
    "address": "Niagara Falls, ON",
    "lat": "",
    "long": "",
    "service": SERVICE_BUS,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/02404/station-details"
}

Stops = [Dundas407, NiagaraFallsBus, NiagaraCollege, Stanley420]