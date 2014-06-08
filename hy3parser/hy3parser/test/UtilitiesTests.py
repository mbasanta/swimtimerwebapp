#!/usr/bin/python
"""
Created on Thu Feb 20 19:55:24 2014

@author: bkant
"""
import unittest
from .. import Utilities

class HY3(unittest.TestCase):
    """Test HY3 data exported from preconfigured Team Manager database"""

    def setUp(self):
        fid = open("hy3parser/test/TestFiles/CCRR-NI-Entries-YMCA STATE CHAMPIONSHIP 2001-16Mar2001-001.HY3")
        self.lines = fid.readlines();
        self.validTestLine = "E1M 8138AnackMB   200E 11 12  0S  4.00  4A  171.37Y  171.37Y    0.00    0.00   NN               N                               40"
    
    def test_checksum(self):
        """Removes checksum from exported HY3 file and tries to recalculate"""
        for line in self.lines:
            line = line.strip()
            output = Utilities.appendCheckSum(line[:-2])
            self.assertEqual(output, line)

class CL2(unittest.TestCase):
    """Test CL2 data exported from preconfigured Team Manager database"""
    
    def setUp(self):
        fid = open("hy3parser/test/TestFiles/CCRR-NI-Entries-YMCA STATE CHAMPIONSHIP 2001-16Mar2001-001.CL2")
        self.lines = fid.readlines();
        self.validTestLine = "A01V3      02Meet Results                  Hy-Tek, Ltd         WMM   3.0Cl Hy-Tek, Ltd       866-456-511112052009                                    MM40    N42"
    
    def test_checksum(self):
        """Removes checksum from exported CL2 file and tries to recalculate"""
        for line in self.lines:
            line = line.strip()
            output = Utilities.appendCheckSum(line[:-4])
            self.assertEqual(output, line)

def run_tests():
    unittest.main()

if __name__ == "__main__":
    run_tests()