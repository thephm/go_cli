# Service Types
SERVICE_TRAIN = "T"

# Location type descriptions in "Stop" 
TRAIN_STATION = "Train Station"
TRAIN_AND_BUS_STATION = "Train & Bus Station"

# -----------------------------------------------------------------------------
# 
# Lines
#
# Line Names, Codes, and Colours (used in ScheduleJourney)
#
# -----------------------------------------------------------------------------

LAKESHORE_EAST_LINE = "Lakeshore East"
LAKESHORE_EAST_LINE_CODE = "LE"

LAKESHORE_WEST_LINE = "Lakeshore West"
LAKESHORE_WEST_LINE_CODE = "LW"

KITCHENER_LINE = "Kitchener"
KITCHENER_LINE_CODE = "GT"

STOUFFVILLE_LINE = "Stoufville"
STOUFFVILLE_LINE_CODE = "ST"

RICHMOND_HILL_LINE = "Richmond Hill"
RICHMOND_HILL_LINE_CODE = "RH"

BARRIE_LINE = "Barrie"
BARRIE_LINE_CODE = "BI"

MILTON_LINE = "Milton"
MILTON_LINE_CODE = "MI"

# -----------------------------------------------------------------------------
# Stop Codes
# 
# Unique label for each train station.
#
# -----------------------------------------------------------------------------

# Union 

UNION_STATION_STOP_CODE = "USTN"

UnionStation = { 
    "code": UNION_STATION_STOP_CODE,
    "type": TRAIN_STATION,
    "name": LAKESHORE_WEST_LINE,
    "code": LAKESHORE_WEST_LINE_CODE,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/un"
}

# Lakeshore West Line Stop Codes
EXHIBITION_STOP_CODE = "EX"
MIMICO_STOP_CODE = "MI"
LONG_BRANCH_STOP_CODE = "LO"
PORT_CREDIT_STOP_CODE = "PO"
CLARKSON_STOP_CODE = "CL"
OAKVILLE_STOP_CODE = "OA"
BRONTE_STOP_CODE = "BO" 
APPLEBY_STOP_CODE = "AP"
BURLINGTON_STOP_CODE = "BU"
ALDERSHOT_STOP_CODE = "AL"
HAMILTON_STOP_CODE = "HA" 
WEST_HARBOUR_STOP_CODE = "WR"
ST_CATHARINES_STOP_CODE = "SCTH"
NIAGARA_FALLS_STOP_CODE = "NI"

Exhibition = { 
    "code": EXHIBITION_STOP_CODE,
    "name": LAKESHORE_WEST_LINE,
    "code": LAKESHORE_WEST_LINE_CODE,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ex",
    "description": ""
}

Mimico = { 
    "code": MIMICO_STOP_CODE,
    "name": LAKESHORE_WEST_LINE,
    "code": LAKESHORE_WEST_LINE_CODE,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/mi",
    "description": ""
}

LongBranch = { 
    "code": LONG_BRANCH_STOP_CODE,
    "name": LAKESHORE_WEST_LINE,
    "code": LAKESHORE_WEST_LINE_CODE,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/lo",
    "description": ""
}

PortCredit = { 
    "code": PORT_CREDIT_STOP_CODE,
    "name": LAKESHORE_WEST_LINE,
    "code": LAKESHORE_WEST_LINE_CODE,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/po",
    "description": ""
}

Clarkson = { 
    "code": CLARKSON_STOP_CODE,
    "name": LAKESHORE_WEST_LINE,
    "code": LAKESHORE_WEST_LINE_CODE,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/cl",
    "description": ""
}

Oakville = { 
    "code": OAKVILLE_STOP_CODE,
    "name": LAKESHORE_WEST_LINE,
    "code": LAKESHORE_WEST_LINE_CODE,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/oa",
    "description": ""
}

Bronte = { 
    "code": BRONTE_STOP_CODE,
    "name": LAKESHORE_WEST_LINE,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/bo",
    "description": ""
}

Appleby = { 
    "code": APPLEBY_STOP_CODE,
    "name": LAKESHORE_WEST_LINE,
    "code": LAKESHORE_WEST_LINE_CODE,
    "type": TRAIN_AND_BUS_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ap",
    "description": ""
}

Burlington = { 
    "code": BURLINGTON_STOP_CODE,
    "name": LAKESHORE_WEST_LINE,
    "code": LAKESHORE_WEST_LINE_CODE,
    "type": TRAIN_AND_BUS_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/bu",
    "description": ""
}

Aldershot = {
    "code": ALDERSHOT_STOP_CODE,
    "name": LAKESHORE_WEST_LINE,
    "code": LAKESHORE_WEST_LINE_CODE,
    "type": TRAIN_AND_BUS_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/al",
    "description": ""
}

Hamilton =  { 
    "code": HAMILTON_STOP_CODE,
    "name": LAKESHORE_WEST_LINE,
    "code": LAKESHORE_WEST_LINE_CODE,
    "type": TRAIN_AND_BUS_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ha",
    "description": ""
}

WestHarbour = { 
    "code": WEST_HARBOUR_STOP_CODE,
    "name": LAKESHORE_WEST_LINE,
    "code": LAKESHORE_WEST_LINE_CODE,
    "type": TRAIN_AND_BUS_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/wr",
    "description": ""
}

StCatharines = { 
    "code": ST_CATHARINES_STOP_CODE,
    "name": LAKESHORE_WEST_LINE,
    "code": LAKESHORE_WEST_LINE_CODE,
    "type": TRAIN_AND_BUS_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/scth",
    "description": "Via"
}

NiagaraFalls = { 
    "code": NIAGARA_FALLS_STOP_CODE,
    "name": LAKESHORE_WEST_LINE,
    "code": LAKESHORE_WEST_LINE_CODE,
    "type": TRAIN_AND_BUS_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ni",
    "description": "Via"
}

# JSON Collection of stations
LakeshoreWestStations = [
    Exhibition, Mimico, LongBranch, PortCredit, Clarkson, 
    Oakville, Bronte, Appleby, Burlington, Aldershot, 
    Hamilton, WestHarbour, StCatharines, NiagaraFalls
]

# Lakeshore East Line Stop Codes
DANFORTH_STOP_CODE = "DA"
SCARBOROUGH_STOP_CODE = "SC"
EGLINGTON_STOP_CODE = "EG"
GUILDWOOD_STOP_CODE = "GU"
ROUGE_HILL_STOP_CODE = "RO"
PICKERING_STOP_CODE = "PIN"
AJAX_STOP_CODE = "AJ"
WHITBY_STOP_CODE = "WH"
OSHAWA_STOP_CODE = "OS"

Danforth = { 
    "code": DANFORTH_STOP_CODE,
    "name": LAKESHORE_EAST_LINE,
    "code": LAKESHORE_EAST_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/da",
    "description": ""
}

Scarborough = { 
    "code": SCARBOROUGH_STOP_CODE,
    "name": LAKESHORE_EAST_LINE,
    "code": LAKESHORE_EAST_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/sc",
    "description": ""
}

Eglington = { 
    "code": EGLINGTON_STOP_CODE,
    "name": LAKESHORE_EAST_LINE,
    "code": LAKESHORE_EAST_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/eg",
    "description": ""
}

Guildwood = { 
    "code": GUILDWOOD_STOP_CODE,
    "name": LAKESHORE_EAST_LINE,
    "code": LAKESHORE_EAST_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/gu",
    "description": ""
}

RougeHill = { 
    "code": ROUGE_HILL_STOP_CODE,
    "name": LAKESHORE_EAST_LINE,
    "code": LAKESHORE_EAST_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ro",
    "description": ""
}

Pickering = { 
    "code": PICKERING_STOP_CODE,
    "name": LAKESHORE_EAST_LINE,
    "code": LAKESHORE_EAST_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/pin",
    "description": ""
}

Ajax = { 
    "code": AJAX_STOP_CODE,
    "name": LAKESHORE_EAST_LINE,
    "code": LAKESHORE_EAST_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/aj",
    "description": ""
}

Whitby = { 
    "code": WHITBY_STOP_CODE,
    "name": LAKESHORE_EAST_LINE,
    "code": LAKESHORE_EAST_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/wh",
    "description": ""
}

Oshawa = { 
    "code": OSHAWA_STOP_CODE,
    "name": LAKESHORE_EAST_LINE,
    "code": LAKESHORE_EAST_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/os",
    "description": "Durham College"
}

# JSON Collection of stations
LakeshoreEastStations = [
    Danforth, Scarborough, Eglington, Guildwood, 
    RougeHill, Pickering, Ajax, Whitby, Oshawa
]

# Barrie Line Stop Codes
DOWNSVIEW_STOP_CODE = "DW" 
RUTHERFORD_STOP_CODE = "RU"
MAPLE_STOP_CODE = "MP" 
KING_CITY_STOP_CODE = "KC"
AURORA_STOP_CODE = "AU"
NEWMARKET_STOP_CODE = "NE"
EAST_GWILLIMBURY_STOP_CODE = "EA"
BRADFORD_STOP_CODE = "BD" 
BARRIE_SOUTH_STOP_CODE = "BA"
ALLANDALE_WATERFRONT_STOP_CODE = "AD"

Downsview = { 
    "code": DOWNSVIEW_STOP_CODE,
    "name": BARRIE_LINE,
    "code": BARRIE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/dw",
    "description": ""
}

Rutherford = { 
    "code": RUTHERFORD_STOP_CODE,
    "name": BARRIE_LINE,
    "code": BARRIE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ru",
    "description": ""
}

Maple = { 
    "code": MAPLE_STOP_CODE,
    "name": BARRIE_LINE,
    "code": BARRIE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/mp",
    "description": ""
}

KingCity = { 
    "code": KING_CITY_STOP_CODE,
    "name": BARRIE_LINE,
    "code": BARRIE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/kc",
    "description": ""
}

Aurora = { 
    "code": AURORA_STOP_CODE,
    "name": BARRIE_LINE,
    "code": BARRIE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/au",
    "description": ""
}

Newmarket = { 
    "code": NEWMARKET_STOP_CODE,
    "name": BARRIE_LINE,
    "code": BARRIE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ne",
    "description": ""
}

EastGwillimbury = { 
    "code": EAST_GWILLIMBURY_STOP_CODE,
    "name": BARRIE_LINE,
    "code": BARRIE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ea",
    "description": ""
}

Bradford = { 
    "code": BRADFORD_STOP_CODE,
    "name": BARRIE_LINE,
    "code": BARRIE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/bd",
    "description": ""
}

BarrieSouth = { 
    "code": BARRIE_SOUTH_STOP_CODE,
    "name": BARRIE_LINE,
    "code": BARRIE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ba",
    "description": ""
}

AllandaleWaterfront = { 
    "code": ALLANDALE_WATERFRONT_STOP_CODE,
    "name": BARRIE_LINE,
    "code": BARRIE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ad",
    "description": ""
}

# JSON Collection of stations
BarrieStations = [
    Downsview, Rutherford, Maple, KingCity, Aurora, Newmarket,
    EastGwillimbury, Bradford, BarrieSouth, AllandaleWaterfront
]

# Kitchener Line Stop Codes
BLOOR_STOP_CODE = "BL"
WESTON_STOP_CODE = "WE"
ETOBICOKE_NORTH_STOP_CODE = "ET"
MALTON_STOP_CODE = "MA" 
BRAMALEA_STOP_CODE = "BE"
BRAMPTON_STOP_CODE = "BR"
MOUNT_PLEASANT_STOP_CODE = "MO"
GEORGETOWN_STOP_CODE = "GE"
ACTON_STOP_CODE = "AC"
GUELPH_STOP_CODE = "GL" 
KITCHENER_STOP_CODE = "KI"

Bloor = { 
    "code": BLOOR_STOP_CODE,
    "name": KITCHENER_LINE,
    "code": KITCHENER_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/bl",
    "description": ""
}

Weston = { 
    "code": WESTON_STOP_CODE,
    "name": KITCHENER_LINE,
    "code": KITCHENER_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/we",
    "description": ""
}

EtobicokeNorth = { 
    "code": ETOBICOKE_NORTH_STOP_CODE,
    "name": KITCHENER_LINE,
    "code": KITCHENER_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/et",
    "description": ""
}

Malton = { 
    "code": MALTON_STOP_CODE,
    "name": KITCHENER_LINE,
    "code": KITCHENER_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ma",
    "description": ""
}

Bramalea = { 
    "code": BRAMALEA_STOP_CODE,
    "name": KITCHENER_LINE,
    "code": KITCHENER_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/be",
    "description": ""
}

Brampton = { 
    "code": BRAMPTON_STOP_CODE,
    "name": KITCHENER_LINE,
    "code": KITCHENER_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/br",
    "description": "Brampton Innovation District",
}

MountPleasant = { 
    "code": MOUNT_PLEASANT_STOP_CODE,
    "name": KITCHENER_LINE,
    "code": KITCHENER_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/mo",
    "description": ""
}

Georgetown = { 
    "code": GEORGETOWN_STOP_CODE,
    "name": KITCHENER_LINE,
    "code": KITCHENER_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ge",
    "description": ""
}

Acton = { 
    "code": ACTON_STOP_CODE,
    "name": KITCHENER_LINE,
    "code": KITCHENER_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ac",
    "description": ""
}

Guelph = { 
    "code": GUELPH_STOP_CODE,
    "name": KITCHENER_LINE,
    "code": KITCHENER_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/gl",
    "description": "Guelph Central"
}

Kitchener = { 
    "code": KITCHENER_STOP_CODE,
    "name": KITCHENER_LINE,
    "code": KITCHENER_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ki",
    "description": ""
}

# JSON Collection of stations
KitchenerStations = [
    Bloor, Weston, EtobicokeNorth, Malton, Bramalea, Brampton,
    MountPleasant, Georgetown, Acton, Guelph, Kitchener
]

# Milton Line Stop Codes
KIPLING_STOP_CODE = "KP"
DIXIE_STOP_CODE = "DI"
COOKSVILLE_STOP_CODE = "CO"
ERINDALE_STOP_CODE = "ER"
STREETSVILLE_STOP_CODE = "SR"
MEADOWVALE_STOP_CODE = "ME"
LISGAR_STOP_CODE = "LS"
MILTON_STOP_CODE = "ML"

Kipling = { 
    "code": KIPLING_STOP_CODE,
    "name": MILTON_LINE,
    "code": MILTON_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/kp",
    "description": ""
}

Dixie = { 
    "code": DIXIE_STOP_CODE,
    "name": MILTON_LINE,
    "code": MILTON_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/di",
    "description": ""
}

Cooksville = { 
    "code": COOKSVILLE_STOP_CODE,
    "name": MILTON_LINE,
    "code": MILTON_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/co",
    "description": ""
}

Erindale = { 
    "code": ERINDALE_STOP_CODE,
    "name": MILTON_LINE,
    "code": MILTON_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/er",
    "description": ""
}

Streetsville = { 
    "code": STREETSVILLE_STOP_CODE,
    "name": MILTON_LINE,
    "code": MILTON_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/sr",
    "description": ""
}

Meadowvale = { 
    "code": MEADOWVALE_STOP_CODE,
    "name": MILTON_LINE,
    "code": MILTON_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/me",
    "description": ""
}

Lisgar = { 
    "code": LISGAR_STOP_CODE,
    "name": MILTON_LINE,
    "code": MILTON_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ls",
    "description": ""
}

Milton = { 
    "code": MILTON_STOP_CODE,
    "name": MILTON_LINE,
    "code": MILTON_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ml",
    "description": ""
}

# JSON Collection of stations
MiltonStations = [
    Kipling, Dixie, Cooksville, Erindale, Streetsville, 
    Meadowvale, Lisgar, Milton
]

# Richmond Hill Line Stop Codes
ORIOLE_STOP_CODE = "OR"
OLD_CUMMER_STOP_CODE = "OL"
LANGSTAFF_STOP_CODE = "LA"
RICHMOND_HILL_STOP_CODE = "RI"
GORMLEY_STOP_CODE = "GO"
BLOOMINGTON_STOP_CODE = "BM"

Oriole = { 
    "code": ORIOLE_STOP_CODE,
    "name": RICHMOND_HILL_LINE,
    "code": RICHMOND_HILL_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/or",
    "description": ""
}

OldCummer = { 
    "code": OLD_CUMMER_STOP_CODE,
    "name": RICHMOND_HILL_LINE,
    "code": RICHMOND_HILL_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ol",
    "description": ""
}

Langstaff = { 
    "code": LANGSTAFF_STOP_CODE,
    "name": RICHMOND_HILL_LINE,
    "code": RICHMOND_HILL_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/la",
    "description": ""
}

RichmondHill = { 
    "code": RICHMOND_HILL_STOP_CODE,
    "name": RICHMOND_HILL_LINE,
    "code": RICHMOND_HILL_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ri",
    "description": ""
}

Gormley = { 
    "code": GORMLEY_STOP_CODE,
    "name": RICHMOND_HILL_LINE,
    "code": RICHMOND_HILL_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/go",
    "description": ""
}

Bloomington = { 
    "code": BLOOMINGTON_STOP_CODE,
    "name": RICHMOND_HILL_LINE,
    "code": RICHMOND_HILL_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/bm",
    "description": ""
}

# JSON Collection of stations
RichmondHillStations = [
    Oriole, OldCummer, Langstaff, RichmondHill, Gormley, Bloomington
]

# Stouffville Line Stop Codes
# DANFORTH = "DA"
SCARBOROUGH_STOP_CODE = "SC"
KENNEDY_STOP_CODE = "KE"
AGINCOURT_STOP_CODE = "AG"
MILLIKEN_STOP_CODE = "MK"
UNIONVILLE_STOP_CODE = "UI"
CENTENNIAL_STOP_CODE = "CE"
MARKHAM_STOP_CODE = "MR"
MOUNT_JOY_STOP_CODE = "MJ"
STOUFFVILLE_STOP_CODE = "ST"
OLD_ELM_STOP_CODE = "LI"      # 

Scarbourough = { 
    "code": SCARBOROUGH_STOP_CODE,
    "name": STOUFFVILLE_LINE,
    "code": STOUFFVILLE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/sc",
    "description": ""
}

Kennedy = { 
    "code": KENNEDY_STOP_CODE,
    "name": STOUFFVILLE_LINE,
    "code": STOUFFVILLE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ke",
    "description": ""
}

Agincourt = { 
    "code": AGINCOURT_STOP_CODE,
    "name": STOUFFVILLE_LINE,
    "code": STOUFFVILLE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ag",
    "description": ""
}

Milliken = { 
    "code": MILLIKEN_STOP_CODE,
    "name": STOUFFVILLE_LINE,
    "code": STOUFFVILLE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/mk",
    "description": ""
}

Unionville = { 
    "code": UNIONVILLE_STOP_CODE,
    "name": STOUFFVILLE_LINE,
    "code": STOUFFVILLE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ui",
    "description": ""
}

Centennial = { 
    "code": CENTENNIAL_STOP_CODE,
    "name": STOUFFVILLE_LINE,
    "code": STOUFFVILLE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/ce",
    "description": ""
}

Markham = { 
    "code": MARKHAM_STOP_CODE,
    "name": STOUFFVILLE_LINE,
    "code": STOUFFVILLE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/mr",
    "description": ""
}

MountJoy = { 
    "code": MOUNT_JOY_STOP_CODE,
    "name": STOUFFVILLE_LINE,
    "code": STOUFFVILLE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/mj",
    "description": ""
}

Stouffville = { 
    "code": STOUFFVILLE_STOP_CODE,
    "name": STOUFFVILLE_LINE,
    "code": STOUFFVILLE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/st",
    "description": ""
}

OldElm = { 
    "code": OLD_ELM_STOP_CODE,
    "name": STOUFFVILLE_LINE,
    "code": STOUFFVILLE_LINE_CODE,
    "type": TRAIN_STATION,
    "service": SERVICE_TRAIN,
    "url": "https://www.gotransit.com/en/find-a-station-or-stop/li",
    "description": ""
}

StouffvilleStations = [
    Danforth, Scarborough, Kennedy, Agincourt, Milliken, Unionville, 
    Centennial, Markham, MountJoy, Stouffville, OldElm
]

LakeshoreEast = {
    "code": LAKESHORE_EAST_LINE_CODE,
    "name": LAKESHORE_EAST_LINE,
    "colour": "#FF0D00",
    "stops": LakeshoreEastStations
}

LakeshoreWest = {
    "name": LAKESHORE_WEST_LINE,
    "code": LAKESHORE_WEST_LINE_CODE,
    "colour": "#98002E",
    "stops": LakeshoreWestStations
}

Barrie = {
    "name": BARRIE_LINE,
    "code": BARRIE_LINE_CODE,
    "colour": "#003767",
    "stops": BarrieStations
}

Milton = {
    "code": MILTON_LINE_CODE,
    "name": MILTON_LINE,
    "colour": "#F57F25",
    "stops": MiltonStations
}

Kitchener = {
    "code": KITCHENER_LINE_CODE,
    "name": KITCHENER_LINE,
    "colour": "#00853E",
    "stops": KitchenerStations
}

Stouffville = {
    "code": STOUFFVILLE_LINE_CODE,
    "name": STOUFFVILLE_LINE,
    "colour": "#794500",
    "stops": StouffvilleStations
}

RichmondHill = {
    "code": RICHMOND_HILL_LINE_CODE,
    "name": RICHMOND_HILL_LINE,
    "colour": "#0099C7",
    "stops": RichmondHillStations
}

Lines = [LakeshoreEast, LakeshoreWest, Barrie, Milton, Kitchener, Stouffville, RichmondHill]
