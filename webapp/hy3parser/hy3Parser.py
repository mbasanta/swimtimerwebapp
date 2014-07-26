#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
"""
HY3 file parser
"""

from hy3parser.constants import LINE_TYPE_CONSTANTS
from hy3parser.line_formats.b_lines import B1Line, B2Line
from hy3parser.line_formats.c_lines import C1Line, C2Line, C3Line
from hy3parser.line_formats.d1_line import D1Line
from hy3parser.line_formats.e1_line import E1Line
from sys import argv

LINE_TYPE = LINE_TYPE_CONSTANTS.LINE_TYPE


def parseFile(inputFile, outputFile):
    text = open(inputFile)
    for line in text.read().splitlines():
        if (line[0:2] == LINE_TYPE_CONSTANTS.LINE_TYPE['SWIMMER_INFO_1']):
            entry = D1Line(line)
            print line[:75]
            print entry.first_name + " '" + entry.nick_name + "' " + \
                entry.last_name
            print str(entry.age) + "/" + entry.gender + " (" + \
                str(entry.date_of_birth.month) + "/" + \
                str(entry.date_of_birth.day) + "/" + \
                str(entry.date_of_birth.year) + ")"


def break_out_lines(input_file):
    file_data = {}
    text = open(input_file)

    for line in text.read().splitlines():

        if (line[0:2] == LINE_TYPE['MEET_INFO']):
            if not LINE_TYPE['MEET_INFO'] in file_data:
                file_data[LINE_TYPE['MEET_INFO']] = []
            file_data[LINE_TYPE['MEET_INFO']].append(B1Line(line))

        if (line[0:2] == LINE_TYPE['MEET_INFO_CONT']):
            if not LINE_TYPE['MEET_INFO_CONT'] in file_data:
                file_data[LINE_TYPE['MEET_INFO_CONT']] = []
            file_data[LINE_TYPE['MEET_INFO_CONT']].append(B2Line(line))

        if (line[0:2] == LINE_TYPE['TEAM_INFO_1']):
            if not LINE_TYPE['TEAM_INFO_1'] in file_data:
                file_data[LINE_TYPE['TEAM_INFO_1']] = []
            file_data[LINE_TYPE['TEAM_INFO_1']].append(C1Line(line))

        if (line[0:2] == LINE_TYPE['TEAM_INFO_2']):
            if not LINE_TYPE['TEAM_INFO_2'] in file_data:
                file_data[LINE_TYPE['TEAM_INFO_2']] = []
            file_data[LINE_TYPE['TEAM_INFO_2']].append(C2Line(line))

        if (line[0:2] == LINE_TYPE['TEAM_INFO_3']):
            if not LINE_TYPE['TEAM_INFO_3'] in file_data:
                file_data[LINE_TYPE['TEAM_INFO_3']] = []
            file_data[LINE_TYPE['TEAM_INFO_3']].append(C3Line(line))

        if (line[0:2] == LINE_TYPE['SWIMMER_INFO_1']):
            if not LINE_TYPE['SWIMMER_INFO_1'] in file_data:
                file_data[LINE_TYPE['SWIMMER_INFO_1']] = []
            file_data[LINE_TYPE['SWIMMER_INFO_1']].append(D1Line(line))

        if (line[0:2] == LINE_TYPE['SWIMMER_INFO_2']):
            pass
        if (line[0:2] == LINE_TYPE['SWIMMER_INFO_3']):
            pass
        if (line[0:2] == LINE_TYPE['SWIMMER_INFO_4']):
            pass
        if (line[0:2] == LINE_TYPE['SWIMMER_INFO_5']):
            pass
        if (line[0:2] == LINE_TYPE['INDIVIDUAL_ENTRY']):
            if not LINE_TYPE['INDIVIDUAL_ENTRY'] in file_data:
                file_data[LINE_TYPE['INDIVIDUAL_ENTRY']] = []
            file_data[LINE_TYPE['INDIVIDUAL_ENTRY']].append(E1Line(line))

        if (line[0:2] == LINE_TYPE['INDIVIDUAL_RESULTS']):
            pass
        if (line[0:2] == LINE_TYPE['RELAY_ENTRY']):
            pass
        if (line[0:2] == LINE_TYPE['RELAY_RESULTS']):
            pass

    text.close()
    return file_data

if __name__ == "__main__":
    file_data = break_out_lines(argv[1])
