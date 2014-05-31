#!/usr/bin/python
# pylint: disable=W0212, R0904

"""Unit tests for C2 Lines"""

import unittest
from ..line_formats.c_lines import C2Line
from ..line_formats import line_format_errors


class C2LineConstructor(unittest.TestCase):
    """Test Constructor for C1Line"""
    good_line = ("C2Jim Beam                      123 Main Street           "
                 "    Lexington                     KY40514     USA USS     "
                 "            21")

    bad_line = ("B1YMCA STATE CHAMPIONSHIP 2001                 Brighton, NY"
                " USA                             031620010318200112012000 1"
                "234       75")

    short_line = "C2ASDFASDF"

    def test_constructor_without_value(self):
        """Test constructor with no value passed"""
        line = C2Line()
        self.assertEqual((line.addr_name,
                          line.addr,
                          line.addr_city,
                          line.addr_state,
                          line.addr_zip,
                          line.addr_country,
                          line.team_reg),
                         (None, None, None, None, None, None, None))

    def test_constructor_with_value(self):
        """Test constructor with line value"""
        line = C2Line(self.good_line)
        self.assertEqual((line.addr_name,
                          line.addr,
                          line.addr_city,
                          line.addr_state,
                          line.addr_zip,
                          line.addr_country,
                          line.team_reg),
                         ("Jim Beam",
                          "123 Main Street",
                          "Lexington",
                          "KY",
                          "40514",
                          "USA",
                          "USS"))

    def test_constructor_short_value(self):
        """Throw InputLineError if an incorrect length line is passed"""
        self.assertRaises(line_format_errors.InputLineError,
                          lambda: C2Line(self.short_line))

    def test_constructor_bad_value(self):
        """Should throw InputLineError if the wrong line type is passed"""
        self.assertRaises(line_format_errors.InputLineError,
                          lambda: C2Line(self.bad_line))


class C2LineAddrName(unittest.TestCase):
    """Test parsing address name"""
    known_values = (
        ("Brothers Promotions (dba FISH)",
            "Brothers Promotions (dba FISH)"),
        ("Dolphins LLC                  ",
            "Dolphins LLC"),
        ("James Ray                     ",
            "James Ray"),
        ("                              ",
            "")
    )

    def setUp(self):
        self.line = C2Line()

    def test_addr_name_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_addr_name(input_val)
            self.assertEqual(output_val, self.line.addr_name)


class C2LineAddr(unittest.TestCase):
    """Test parsing address"""
    known_values = (
        ("123 Main Street               ",
            "123 Main Street"),
        ("120 Crescent Lane             ",
            "120 Crescent Lane"),
        ("PO Box 1409                   ",
            "PO Box 1409"),
        ("                              ",
            "")
    )

    def setUp(self):
        self.line = C2Line()

    def test_addr_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_addr(input_val)
            self.assertEqual(output_val, self.line.addr)


class C2LineAddrCity(unittest.TestCase):
    """Test parsing address city"""
    known_values = (
        ("Lexington                     ",
            "Lexington"),
        ("Cleveland                     ",
            "Cleveland"),
        ("New York                      ",
            "New York"),
        ("                              ",
            "")
    )

    def setUp(self):
        self.line = C2Line()

    def test_addr_city_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_addr_city(input_val)
            self.assertEqual(output_val, self.line.addr_city)


class C2LineAddrState(unittest.TestCase):
    """Test parsing address state"""
    known_values = (
        ("KY",
            "KY"),
        ("NY",
            "NY"),
        ("CA",
            "CA"),
        ("  ",
            "")
    )

    bad_values = ("12",
                  "k1",
                  "1 ")

    def setUp(self):
        self.line = C2Line()

    def test_addr_state_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_addr_state(input_val)
            self.assertEqual(output_val, self.line.addr_state)

    def test_addr_state_bad_values(self):
        """Raise FieldParseError for invalid state"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_addr_state(val))


class C2LineAddrZip(unittest.TestCase):
    """Test parsing address zip"""
    known_values = (
        ("40514-1234",
            "40514-1234"),
        ("40517     ",
            "40517"),
        ("     40213",
            "40213"),
        ("          ",
            "")
    )

    bad_values = ("        12",
                  "        k1",
                  "40514-abdc")

    def setUp(self):
        self.line = C2Line()

    def test_addr_zip_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_addr_zip(input_val)
            self.assertEqual(output_val, self.line.addr_zip)

    def test_addr_zip_bad_values(self):
        """Raise FieldParseError for invalid zip"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_addr_zip(val))


class C2LineAddrCountry(unittest.TestCase):
    """Test parsing address country"""
    known_values = (
        (" NZ",
            "NZ"),
        ("GB ",
            "GB"),
        ("USA",
            "USA"),
        ("   ",
            "")
    )

    bad_values = (" 12",
                  " k1",
                  "405")

    def setUp(self):
        self.line = C2Line()

    def test_addr_country_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_addr_country(input_val)
            self.assertEqual(output_val, self.line.addr_country)

    def test_addr_country_bad_values(self):
        """Raise FieldParseError for invalid country"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_addr_country(val))


class C2LineTeamReg(unittest.TestCase):
    """Test parsing team type from string"""
    known_values = (("aust", "AUST"),
                    ("AUST", "AUST"),
                    ("bcss", "BCSS"),
                    ("BCSS", "BCSS"),
                    ("nzsf", "NZSF"),
                    ("NZSF", "NZSF"),
                    ("oth", "OTH"),
                    ("OTH", "OTH"),
                    ("ssa", "SSA"),
                    ("SSA", "SSA"),
                    ("uk", "UK"),
                    ("UK", "UK"),
                    ("uss", "USS"),
                    ("USS", "USS"))

    bad_values = ("uk1",
                  "18",
                  "asdf",
                  "ASD")

    def setUp(self):
        self.line = C2Line()

    def test_team_reg_bad_value(self):
        """Raise FieldParseError for invalid team reg"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_team_reg(val))

    def test_team_reg_good_values(self):
        """Parse valid team reg codes successfully"""
        for input_val, output_val in self.known_values:
            self.line._parse_team_reg(input_val)
            self.assertEqual(output_val, self.line.team_reg)

    def test_team_reg_no_value(self):
        """Set team reg to None if value is empty string"""
        self.line._parse_team_reg("    ")
        self.assertEqual(self.line.team_reg, None)


def run_tests():
    """Execute the tests"""
    unittest.main()


if __name__ == "__main__":
    run_tests()
