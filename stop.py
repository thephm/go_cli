CODE = "StopCode"      # what it is called in API calls

NEW_LINE = "\n"

class Stop:
    def __init__(self):
        self.code = ""     # two letter code for this stop
        self.line = self.Line() # the Line that the stop is on

    def __str__(self):
        output = "code: " + self.id + NEW_LINE
        output += "line: " + str(self.line) + NEW_LINE
        return output