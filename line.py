CODE = "LineCode"
NAME = "LineName"

NEW_LINE = "\n"

class Line:
    def __init__(self):
        self.code = ""          # two letter code for this line e.g. "LW"
        self.name = ""          # line name e.g. Lakeshore West
        self.service_type = ""  # e.g. go_train.SERVICE_TRAIN
        self.stops = []         # stops on the line 

    def __str__(self):
        output = "code: " + self.code + NEW_LINE
        output += "name: " + self.name + NEW_LINE
        output += "service_type: " +  self.service_type + NEW_LINE
        output += "stops: " +  str(self.stops) + NEW_LINE
        return output