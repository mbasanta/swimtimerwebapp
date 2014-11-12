# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:41:07 2014

@author: bkant
"""
from math import floor

HY3FileLength = 128
HY3Scale = 21
HY3Offset = 205

CL2FileLength = 156
CL2Scale = 19
CL2Offset = 211


class CheckSumExportException(Exception):
    """Exception to throw when there's an error in the creation of checksum"""
    def __init__(self, field):
        Exception.__init__(self)
        self.field = field
        self.message = "Error creating checksum " + field

    def __str__(self):
        return repr(self.message)


class MultipleLinesFoundException(Exception):
    """
    Exception to throw when parsing a file and more lines then expected
    are found
    """
    def __init__(self):
        Exception.__init__(self)
        self.message = "Multiple lines found, only one line expected"

    def __str__(self):
        return repr(self.message)


def append_check_sum(input_str, file_format=None):
    """
    append_check_sum is used for exporting Team Manager/Meet Manager
    compliant files.
    Parameters:
    -inputStr: string to be written to file.  It must be the correct length
    (HY3-128 characters, CL2-156 characters).
    -fileFormat: string indicating desired file format (HY3/CL2)
    """
    # check if inputStr is a string
    if not isinstance(input_str, unicode):
        raise CheckSumExportException("input_str parameter is not a string")

    #check if fileFormat is specified and if it is, if it is a string
    if file_format is None:
        if len(input_str) == HY3FileLength:
            file_format = "HY3"
        elif len(input_str) == CL2FileLength:
            file_format = "CL2"
        else:
            raise CheckSumExportException("inputStr is not the correct " +
                                          "length for either CL2 or HY3")
    elif not isinstance(file_format, unicode):
        raise CheckSumExportException("fileFormat parameter is not a string")
    else:
        if input_str.upper() == "HY3":
            file_format = "HY3"
        elif input_str.upper() == "CL2":
            file_format = "CL2"
        else:
            raise CheckSumExportException("fileFormat parameter is \
                neither HY3 nor CL2")

    if file_format == "HY3":
        evens = input_str[::2]
        evens_sum = sequence_sum(evens)

        odds = input_str[1::2]
        odds_sum = sequence_sum(odds)

        total = evens_sum + 2*odds_sum

        final = unicode(int(floor(total/HY3Scale) + HY3Offset))

        return input_str + final[-1] + final[-2]
    else:  # CL2
        total = sequence_sum(input_str)

        final = unicode(int(floor(total/CL2Scale) + CL2Offset))

        suffix = ""
        if input_str.startswith("DO"):
            suffix += "NN"
        else:
            suffix += " N"

        return input_str + suffix + final[-1] + final[-2]


def sequence_sum(char_sequence):
    '''Calc sum of sequence of characters'''
    seq_sum = 0
    for char in char_sequence:
        seq_sum += ord(char)

    return seq_sum


def vals_from_dict(dictionary):
    """
    Return a dictionary iterator that python v2 or v3 compatible
    """
    try:
        return dictionary.itervalues()
    except AttributeError:
        return dictionary.values()
