#!/usr/bin/python
# pylint: disable=W0212, R0904

"""Unit tests for C1 Lines"""

import unittest
from ..line_formats.c_lines import C1Line
from ..line_formats import line_format_errors


class C1LineConstructor(unittest.TestCase):
    """Test Constructor for C1Line"""
    good_line = ("C1DolphDolphin's Swim Team           Dolphin's       LL   "
                 "                                                          "
                 "   AGE      81")

    bad_line = ("B1YMCA STATE CHAMPIONSHIP 2001                 Brighton, NY"
                " USA                             031620010318200112012000 1"
                "234       75")

    short_line = "C1ASDFASDF"

    def test_constructor_without_value(self):
        """Test constructor with no value passed"""
        line = C1Line()
        self.assertEqual((line.team_abbr,
                          line.team_name,
                          line.team_short_name,
                          line.team_type),
                         (None, None, None, None))

    def test_constructor_with_value(self):
        """Test constructor with line value"""
        line = C1Line(self.good_line)
        self.assertEqual((line.team_abbr,
                          line.team_name,
                          line.team_short_name,
                          line.team_type),
                         ("Dolph",
                          "Dolphin's Swim Team",
                          "Dolphin's",
                          "AGE"))

    def test_constructor_short_value(self):
        """Throw InputLineError if an incorrect length line is passed"""
        self.assertRaises(line_format_errors.InputLineError,
                          lambda: C1Line(self.short_line))

    def test_constructor_bad_value(self):
        """Should throw InputLineError if the wrong line type is passed"""
        self.assertRaises(line_format_errors.InputLineError,
                          lambda: C1Line(self.bad_line))


class C1LineTeamAbbr(unittest.TestCase):
    """Test parsing team abbr"""
    known_values = (
        ("Fish ", "Fish"),
        ("Dolph", "Dolph"),
        ("May's", "May's"),
        ("     ", "")
    )

    def setUp(self):
        self.line = C1Line()

    def test_team_abbr_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_team_abbr(input_val)
            self.assertEqual(output_val, self.line.team_abbr)


class C1LineTeamName(unittest.TestCase):
    """Test parsing team name"""
    known_values = (
        ("Fish Team Swimmers            ",
            "Fish Team Swimmers"),
        ("Dolphins Speeders             ",
            "Dolphins Speeders"),
        ("May's Marlins                 ",
            "May's Marlins"),
        ("                              ",
            "")
    )

    def setUp(self):
        self.line = C1Line()

    def test_team_name_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_team_name(input_val)
            self.assertEqual(output_val, self.line.team_name)


class C1LineTeamShortName(unittest.TestCase):
    """Test parsing team short name"""
    known_values = (
        ("Fish Swimmers   ",
            "Fish Swimmers"),
        ("Dolphins        ",
            "Dolphins"),
        ("May's Marlins   ",
            "May's Marlins"),
        ("                ",
            "")
    )

    def setUp(self):
        self.line = C1Line()

    def test_short_name_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_team_short_name(input_val)
            self.assertEqual(output_val, self.line.team_short_name)


class C1LineTeamType(unittest.TestCase):
    """Test parsing team type from string"""
    known_values = (("age", "AGE"),
                    ("AGE", "AGE"),
                    ("hs", "HS"),
                    ("HS", "HS"),
                    ("col", "COL"),
                    ("COL", "COL"),
                    ("mas", "MAS"),
                    ("MAS", "MAS"),
                    ("oth", "OTH"),
                    ("OTH", "OTH"),
                    ("rec", "REC"),
                    ("REC", "REC"))

    bad_values = ("xx",
                  "18",
                  "asdf",
                  "ASD")

    def setUp(self):
        self.line = C1Line()

    def test_team_type_bad_value(self):
        """Raise FieldParseError for invalid team type"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_team_type(val))

    def test_team_type_good_values(self):
        """Parse valid team type codes successfully"""
        for input_val, output_val in self.known_values:
            self.line._parse_team_type(input_val)
            self.assertEqual(output_val, self.line.team_type)

    def test_team_type_no_value(self):
        """Set team type to None if value is empty string"""
        self.line._parse_team_type("   ")
        self.assertEqual(self.line.team_type, None)


def run_tests():
    """Execute the tests"""
    unittest.main()


if __name__ == "__main__":
    run_tests()
