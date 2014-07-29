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


def appendCheckSum(inputStr, fileFormat=None):
    """appendCheckSum is used for exporting Team Manager/Meet Manager compliant
    files. 
    Parameters:
    -inputStr: string to be written to file.  It must be the correct length (
    HY3-128 characters, CL2-156 characters).
    -fileFormat: string indicating desired file format (HY3/CL2)"""
    
    #check if inputStr is a string
    if (not isinstance(inputStr,str)):
        raise CheckSumExportException("inputStr parameter is not a string")
    
    #check if fileFormat is specified and if it is, if it is a string
    if (fileFormat == None):
        if (len(inputStr) == HY3FileLength):
            fileFormat = "HY3"
        elif (len(inputStr) == CL2FileLength):
            fileFormat = "CL2"
        else:
            raise CheckSumExportException("inputStr is not the correct length for either CL2 or HY3")
    elif (not isinstance(fileFormat,str)):
        raise CheckSumExportException("fileFormat parameter is not a string")
    else:
        if (inputStr.upper() == "HY3"):
            fileFormat = "HY3"
        elif (inputStr.upper() == "CL2"):
            fileFormat = "CL2"
        else:
            raise CheckSumExportException("fileFormat parameter is neither HY3 nor CL2")
    
    if (fileFormat == "HY3"):
        evens = inputStr[::2]
        evensSum = sequenceSum(evens)
        
        odds = inputStr[1::2]
        oddsSum = sequenceSum(odds)
        
        total = evensSum + 2*oddsSum
        
        final = str(int(floor(total/HY3Scale) + HY3Offset))
        
        return inputStr + final[-1] + final[-2]
    else: #CL2
        total = sequenceSum(inputStr)
        
        final = str(int(floor(total/CL2Scale) + CL2Offset))
        
        suffix = ""
        if (inputStr.startswith("DO")):
            suffix += "NN"
        else:
            suffix += " N"
        
        return inputStr + suffix + final[-1] + final[-2]
        
def sequenceSum(charSequence):
    seqSum = 0;
    for c in charSequence:
        seqSum += ord(c)
    
    return seqSum
