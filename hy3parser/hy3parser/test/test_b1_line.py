#!/usr/bin/python
# pylint: disable=W0212, R0904

"""Unit tests for B1 Lines"""

import unittest
import datetime
from ..line_formats.b_lines import B1Line
from ..line_formats import line_format_errors


class B1LineConstructor(unittest.TestCase):
    """Test Constructor for B1Line"""
    test_line = ("B1YMCA STATE CHAMPIONSHIP 2001                 Brighton, NY"
                 " USA                             031620010318200112012000 1"
                 "234       75")

    bad_line = ("E1F14081Reed                Laramie                         "
                "        J021100LARJREED 101902112000  9     0               "
                "        11")

    short_line = "D1ASDFASDF"

    def test_constructor_without_value(self):
        """Test constructor with no value passed"""
        line = B1Line()
        self.assertEqual((line.meet_name,
                          line.facility,
                          line.start_date,
                          line.end_date,
                          line.age_up_date,
                          line.elevation),
                         (None, None, None, None, None, None))

    def test_constructor_with_value(self):
        """Test constructor with line value"""
        line = B1Line(self.test_line)
        self.assertEqual((line.meet_name,
                          line.facility,
                          line.start_date,
                          line.end_date,
                          line.age_up_date,
                          line.elevation),
                         ("YMCA STATE CHAMPIONSHIP 2001",
                          "Brighton, NY USA",
                          datetime.date(2001, 3, 16),
                          datetime.date(2001, 3, 18),
                          datetime.date(2000, 12, 1),
                          1234))

    def test_constructor_short_value(self):
        """Throw InputLineError if an incorrect length line is passed"""
        self.assertRaises(line_format_errors.InputLineError,
                          lambda: B1Line(self.short_line))

    def test_constructor_bad_value(self):
        """Should throw InputLineError if the wrong line type is passed"""
        self.assertRaises(line_format_errors.InputLineError,
                          lambda: B1Line(self.bad_line))


class B1LineMeetName(unittest.TestCase):
    """Test parsing last name"""
    known_values = (
        ("Lexington YMCA Spring Meet                   ",
            "Lexington YMCA Spring Meet"),
        ("Smith-Jones Stallion's                       ",
            "Smith-Jones Stallion's"),
        ("Dodge&Cox 500                                ",
            "Dodge&Cox 500"),
        ("                                             ",
            "")
    )

    def setUp(self):
        self.line = B1Line()

    def test_meet_name_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_meet_name(input_val)
            self.assertEqual(output_val, self.line.meet_name)


class B1LineFacility(unittest.TestCase):
    """Test parsing facility name"""
    known_values = (
        ("Lexington YMCA                               ",
            "Lexington YMCA"),
        ("High@Main pool                               ",
            "High@Main pool"),
        ("Dodge&Cox Stadium                            ",
            "Dodge&Cox Stadium"),
        ("                                             ",
            "")
    )

    def setUp(self):
        self.line = B1Line()

    def test_facility_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_facility(input_val)
            self.assertEqual(output_val, self.line.facility)


class B1LineStartDate(unittest.TestCase):
    """Test parsing event start date"""
    known_values = (("02211981", datetime.date(1981, 2, 21)),
                    ("12012001", datetime.date(2001, 12, 1)),
                    ("01011996", datetime.date(1996, 1, 1)))

    bad_values = ("1   1   ",
                  "abcdefgh",
                  "022I1981",
                  "00000000",
                  "31121985",
                  "02213981")

    def setUp(self):
        self.line = B1Line()

    def test_start_date_bad_value(self):
        """Raise FieldParseError if value can't be parsed to a date"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_start_date(val))

    def test_start_date_good_values(self):
        """Parse date from a string"""
        for input_val, output_val in self.known_values:
            self.line._parse_start_date(input_val)
            self.assertEqual(output_val, self.line.start_date)

    def test_start_date_no_value(self):
        """Set start_date to none if string is empty"""
        self.line._parse_start_date("        ")
        self.assertEqual(None, self.line.start_date)


class B1LineEndDate(unittest.TestCase):
    """Test parsing event end date"""
    known_values = (("02211981", datetime.date(1981, 2, 21)),
                    ("12012001", datetime.date(2001, 12, 1)),
                    ("01011996", datetime.date(1996, 1, 1)))

    bad_values = ("1   1   ",
                  "abcdefgh",
                  "022I1981",
                  "00000000",
                  "31121985",
                  "02213981")

    def setUp(self):
        self.line = B1Line()

    def test_end_date_bad_value(self):
        """Raise FieldParseError if value can't be parsed to a date"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_end_date(val))

    def test_end_date_good_values(self):
        """Parse date from a string"""
        for input_val, output_val in self.known_values:
            self.line._parse_end_date(input_val)
            self.assertEqual(output_val, self.line.end_date)

    def test_end_date_no_value(self):
        """Set end_date to none if string is empty"""
        self.line._parse_end_date("        ")
        self.assertEqual(None, self.line.end_date)


class B1LineAgeUpDate(unittest.TestCase):
    """Test parsing event age up date"""
    known_values = (("02211981", datetime.date(1981, 2, 21)),
                    ("12012001", datetime.date(2001, 12, 1)),
                    ("01011996", datetime.date(1996, 1, 1)))

    bad_values = ("1   1   ",
                  "abcdefgh",
                  "022I1981",
                  "00000000",
                  "31121985",
                  "02213981")

    def setUp(self):
        self.line = B1Line()

    def test_age_up_date_bad_value(self):
        """Raise FieldParseError if value can't be parsed to a date"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_age_up_date(val))

    def test_age_up_date_good_values(self):
        """Parse date from a string"""
        for input_val, output_val in self.known_values:
            self.line._parse_age_up_date(input_val)
            self.assertEqual(output_val, self.line.age_up_date)

    def test_age_up_date_no_value(self):
        """Set age_up_date to none if string is empty"""
        self.line._parse_age_up_date("        ")
        self.assertEqual(None, self.line.age_up_date)


class B1LineElevation(unittest.TestCase):
    """Test parsing elevation"""
    known_values = (("    1", 1),
                    ("   21", 21),
                    ("  321", 321),
                    (" 4321", 4321),
                    ("54321", 54321))

    bad_values = ("1   1",
                  "abcde")

    def setUp(self):
        self.line = B1Line()

    def test_elevation_bad_value(self):
        """Raise FieldParseError if value can't be parsed to a integer"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_elevation(val))

    def test_elevation_good_values(self):
        """Parse integer from a string"""
        for input_val, output_val in self.known_values:
            self.line._parse_elevation(input_val)
            self.assertEqual(output_val, self.line.elevation)

    def test_elevation_no_value(self):
        """Set elevation to none if string is empty"""
        self.line._parse_elevation("     ")
        self.assertEqual(None, self.line.elevation)


def run_tests():
    """Execute the tests"""
    unittest.main()


if __name__ == "__main__":
    run_tests()
