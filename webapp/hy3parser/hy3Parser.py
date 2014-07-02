#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
"""
HY3 file parser
"""

from hy3parser.Constants import LINE_TYPE
from hy3parser.LineFormats import D1Line
from sys import argv


def parseFile(inputFile, outputFile):
    text = open(inputFile)
    for line in text.readlines():
        if (line[0:2] == LINE_TYPE.SWIMMER_INFO_1):
            entry = D1Line(line)
            print line[:75]
            print entry.first_name + " '" + entry.nick_name + "' " + entry.last_name
            print str(entry.age) + "/" + entry.gender + " (" + \
                str(entry.date_of_birth.month) + "/" + \
                str(entry.date_of_birth.day) + "/" + \
                str(entry.date_of_birth.year) + ")"

if __name__ == "__main__":
    parseFile(argv[1], "output.xml")
