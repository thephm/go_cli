"""Facility data returned by the stop details endpoint.

Example source endpoint:
    https://api.openmetrolinx.com/OpenDataAPI/api/V1/Stop/Details/AP

Examples usually omit response fields unrelated to facilities.
"""
    
class Facility:
    def __init__(self):
        self.code = ""           # e.g. "BR"
        self.description = ""    # e.g. "Bicycle Rack"
        self.description_fr = "" # e.g. "Support à bicyclettes"

    CODE = "Code"
    DESCRIPTION = "Description"
    DESCRIPTION_FR = "DescriptionFr"
    
    def parse(self, json_facility):
        try:
            self.code = json_facility[self.CODE]
            self.description = json_facility[self.DESCRIPTION]
            self.description_fr = json_facility[self.DESCRIPTION_FR]
        except:
            pass

    def __str__(self):
        NEW_LINE = "\n"
        output = "code: " + self.code + NEW_LINE
        output += "description: " + str(self.description) + NEW_LINE
        output += "description_fr: " + str(self.description_fr) + NEW_LINE