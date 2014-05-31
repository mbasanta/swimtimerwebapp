#!/usr/bin/python
# pylint: disable=W0212, R0904

"""Unit tests for C3 Lines"""

import unittest
from ..line_formats.c_lines import C3Line
from ..line_formats import line_format_errors


class C2LineConstructor(unittest.TestCase):
    """Test Constructor for C1Line"""
    good_line = ("C3                              1-888-123-4567      1-800"
                 "-789-1234      1-606-543-9999      none@none.com         "
                 "              70")

    bad_line = ("C2Jim Beam                      123 Main Street           "
                "    Lexington                     KY40514     USA USS     "
                "            21")

    short_line = "C3ASDFASDF"

    def test_constructor_without_value(self):
        """Test constructor with no value passed"""
        line = C3Line()
        self.assertEqual((line.daytime_phone,
                          line.evening_phone,
                          line.fax,
                          line.email),
                         (None, None, None, None))

    def test_constructor_with_value(self):
        """Test constructor with line value"""
        line = C3Line(self.good_line)
        self.assertEqual((line.daytime_phone,
                          line.evening_phone,
                          line.fax,
                          line.email),
                         ("1-888-123-4567",
                          "1-800-789-1234",
                          "1-606-543-9999",
                          "none@none.com"))

    def test_constructor_short_value(self):
        """Throw InputLineError if an incorrect length line is passed"""
        self.assertRaises(line_format_errors.InputLineError,
                          lambda: C3Line(self.short_line))

    def test_constructor_bad_value(self):
        """Should throw InputLineError if the wrong line type is passed"""
        self.assertRaises(line_format_errors.InputLineError,
                          lambda: C3Line(self.bad_line))


class C3DaytimePhone(unittest.TestCase):
    """Test parsing daytime phone"""
    known_values = (
        ("567.1234           ",
            "567.1234"),
        ("1 (503) 854-5643   ",
            "1 (503) 854-5643"),
        ("1-859-123-4567     ",
            "1-859-123-4567"),
        ("                   ",
            "")
    )

    def setUp(self):
        self.line = C3Line()

    def test_daytime_phone_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_daytime_phone(input_val)
            self.assertEqual(output_val, self.line.daytime_phone)


class C3EveningPhone(unittest.TestCase):
    """Test parsing evening phone"""
    known_values = (
        ("567.1234           ",
            "567.1234"),
        ("1 (503) 854-5643   ",
            "1 (503) 854-5643"),
        ("1-859-123-4567     ",
            "1-859-123-4567"),
        ("                   ",
            "")
    )

    def setUp(self):
        self.line = C3Line()

    def test_evening_phone_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_evening_phone(input_val)
            self.assertEqual(output_val, self.line.evening_phone)


class C3Fax(unittest.TestCase):
    """Test parsing fax number"""
    known_values = (
        ("567.1234           ",
            "567.1234"),
        ("1 (503) 854-5643   ",
            "1 (503) 854-5643"),
        ("1-859-123-4567     ",
            "1-859-123-4567"),
        ("                   ",
            "")
    )

    def setUp(self):
        self.line = C3Line()

    def test_fax_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_fax(input_val)
            self.assertEqual(output_val, self.line.fax)


class C3Email(unittest.TestCase):
    """Test parsing email"""
    known_values = (
        ("joe.smith.2@aol.com                ",
            "joe.smith.2@aol.com"),
        ("thisguy@another.email.net          ",
            "thisguy@another.email.net"),
        ("someone.else@gmail.com             ",
            "someone.else@gmail.com"),
        ("                                   ",
            "")
    )

    def setUp(self):
        self.line = C3Line()

    def test_email_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_email(input_val)
            self.assertEqual(output_val, self.line.email)
