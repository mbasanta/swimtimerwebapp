"""Custom Error classes for parsing HY3 lines"""


class FieldParseError(Exception):
    """Error to throw when there's a error parsing a field from the line"""
    def __init__(self, field):
        Exception.__init__(self)
        self.field = field
        self.message = "Error parsing " + field

    def __str__(self):
        return repr(self.message)


class InputLineError(Exception):
    """Error to throw when the line passed is not correctly formatted"""
    def __init__(self):
        Exception.__init__(self)
        self.message = "Input line not properly formatted"

    def __str__(self):
        return repr(self.message)
