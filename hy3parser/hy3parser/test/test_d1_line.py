#!/usr/bin/python
# pylint: disable=W0212, R0904

"""Unit tests for D1 Lines"""

import unittest
import datetime
from ..line_formats.d1_line import D1Line
from ..line_formats import line_format_errors


class D1LineConstructor(unittest.TestCase):
    """Test Constructor for D1Line"""
    test_line = ("D1F14081Reed                Laramie                        "
                 "         J021100LARJREED 101902112000  9     0             "
                 "          11")

    bad_line = ("E1F14081Reed                Laramie                         "
                "        J021100LARJREED 101902112000  9     0               "
                "        11")

    short_line = "D1ASDFASDF"

    def test_constructor_without_value(self):
        """Test constructor with no value passed"""
        line = D1Line()
        self.assertEqual((line.gender,
                          line.event_swimmer_id,
                          line.last_name,
                          line.first_name,
                          line.nick_name,
                          line.middle_initial,
                          line.uss_num,
                          line.team_swimmer_id,
                          line.date_of_birth,
                          line.age),
                         (None, None, None, None, None,
                          None, None, None, None, None))

    def test_constructor_with_value(self):
        """Test constructor with line value"""
        line = D1Line(self.test_line)
        self.assertEqual((line.gender,
                          line.event_swimmer_id,
                          line.last_name,
                          line.first_name,
                          line.nick_name,
                          line.middle_initial,
                          line.uss_num,
                          line.team_swimmer_id,
                          line.date_of_birth,
                          line.age),
                         ("F",
                          14081,
                          "Reed",
                          "Laramie",
                          "",
                          "J",
                          "021100LARJREED",
                          1019,
                          datetime.date(2000, 2, 11),
                          9))

    def test_constructor_short_value(self):
        """Throw InputLineError if an incorrect length line is passed"""
        self.assertRaises(line_format_errors.InputLineError,
                          lambda: D1Line(self.short_line))

    def test_constructor_bad_value(self):
        """Should throw InputLineError if the wrong line type is passed"""
        self.assertRaises(line_format_errors.InputLineError,
                          lambda: D1Line(self.bad_line))


class D1LineGender(unittest.TestCase):
    """Test parsing genders"""
    known_values = (("M", "M"),
                    ("m", "M"),
                    ("F", "F"),
                    ("f", "F"))

    bad_values = ("x",
                  " ")

    def setUp(self):
        self.line = D1Line()

    def test_gender_bad_value(self):
        """Raise FieldParseError for gender if not M/F"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_gender(val))

    def test_gender_good_values(self):
        """Parse M,m,F,f successfully"""
        for input_val, output_val in self.known_values:
            self.line._parse_gender(input_val)
            self.assertEqual(output_val, self.line.gender)


class D1LineEventSwimmerId(unittest.TestCase):
    """Test parsing event swimmer id"""
    known_values = (("    1", 1),
                    ("   21", 21),
                    ("  321", 321),
                    (" 4321", 4321),
                    ("54321", 54321))

    bad_values = ("1   1",
                  "abcde")

    def setUp(self):
        self.line = D1Line()

    def test_id_bad_value(self):
        """Raise FieldParseError if value can't be parsed to a integer"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_event_swimmer_id(val))

    def test_id_good_values(self):
        """Parse integer from a string"""
        for input_val, output_val in self.known_values:
            self.line._parse_event_swimmer_id(input_val)
            self.assertEqual(output_val, self.line.event_swimmer_id)

    def test_id_no_value(self):
        """Set event_swimmer_id to none if string is empty"""
        self.line._parse_event_swimmer_id("     ")
        self.assertEqual(None, self.line.event_swimmer_id)


class D1LineLastName(unittest.TestCase):
    """Test parsing last name"""
    known_values = (("Smith               ", "Smith"),
                    ("Smith Jones         ", "Smith Jones"),
                    ("Smith III           ", "Smith III"),
                    ("                    ", ""))

    def setUp(self):
        self.line = D1Line()

    def test_last_name_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_last_name(input_val)
            self.assertEqual(output_val, self.line.last_name)


class D1LineFirstName(unittest.TestCase):
    """Test parsing first name"""
    known_values = (("Smith               ", "Smith"),
                    ("Smith Jones         ", "Smith Jones"),
                    ("Smith III           ", "Smith III"),
                    ("                    ", ""))

    def setUp(self):
        self.line = D1Line()

    def test_first_name_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_first_name(input_val)
            self.assertEqual(output_val, self.line.first_name)


class D1LineNickName(unittest.TestCase):
    """Test parsing nick name"""
    known_values = (("Smith               ", "Smith"),
                    ("Smith Jones         ", "Smith Jones"),
                    ("Smith III           ", "Smith III"),
                    ("                    ", ""))

    def setUp(self):
        self.line = D1Line()

    def test_nick_name_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_nick_name(input_val)
            self.assertEqual(output_val, self.line.nick_name)


class D1LineMiddleInitial(unittest.TestCase):
    """Test parsing middle initial"""
    known_values = (("S", "S"),
                    (" ", ""))

    def setUp(self):
        self.line = D1Line()

    def test_middle_initial_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_middle_initial(input_val)
            self.assertEqual(output_val, self.line.middle_initial)


class D1LineUssNum(unittest.TestCase):
    """Test parsing US Swimming Number"""
    known_values = (("011553CATADURA", "011553CATADURA"),
                    ("091879CY*VYOUN", "091879CY*VYOUN"),
                    ("020981THO*CHU*", "020981THO*CHU*"),
                    ("011873TY**    ", "011873TY**"))

    bad_values = ("asdf asdf     ",
                  "123 12     123",
                  "ASDF-ASDF-ASDF")

    def setUp(self):
        self.line = D1Line()

    def test_uss_num_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_uss_num(input_val)
            self.assertEqual(output_val, self.line.uss_num)

    def test_uss_num_bad_values(self):
        """Raise FieldParseError if uss_num contains invalid values"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_uss_num(val))

    def test_uss_num_no_value(self):
        """Set uss_num to none if string is empty"""
        self.line._parse_uss_num("             ")
        self.assertEqual(None, self.line.uss_num)


class D1LineTeamSwimmerId(unittest.TestCase):
    """Test parsing team swimmer id"""
    known_values = (("    1", 1),
                    ("   21", 21),
                    ("  321", 321),
                    (" 4321", 4321),
                    ("54321", 54321))

    bad_values = ("1   1",
                  "abcde")

    def setUp(self):
        self.line = D1Line()

    def test_id_bad_value(self):
        """Raise FieldParseError if value can't be parsed to a integer"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_team_swimmer_id(val))

    def test_id_good_values(self):
        """Parse integer from a string"""
        for input_val, output_val in self.known_values:
            self.line._parse_team_swimmer_id(input_val)
            self.assertEqual(output_val, self.line.team_swimmer_id)

    def test_id_no_value(self):
        """Set team_swimmer_id to none if string is empty"""
        self.line._parse_team_swimmer_id("     ")
        self.assertEqual(None, self.line.team_swimmer_id)


class D1LineDateOfBirth(unittest.TestCase):
    """Test parsing date of birth"""
    known_values = (("02211981", datetime.date(1981, 2, 21)),
                    ("12012001", datetime.date(2001, 12, 1)),
                    ("01011996", datetime.date(1996, 1, 1)))

    bad_values = ("1   1   ",
                  "abcdefgh",
                  "022I1981",
                  "        ",
                  "00000000",
                  "31121985",
                  "02213981")

    def setUp(self):
        self.line = D1Line()

    def test_date_of_birth_bad_value(self):
        """Raise FieldParseError if value can't be parsed to a date"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_date_of_birth(val))

    def test_date_of_birth_good_values(self):
        """Parse date from a string"""
        for input_val, output_val in self.known_values:
            self.line._parse_date_of_birth(input_val)
            self.assertEqual(output_val, self.line.date_of_birth)


class D1LineAge(unittest.TestCase):
    """Test parsing swimmer age"""
    known_values = ((" 1", 1),
                    ("9 ", 9),
                    ("21", 21),
                    (" 9", 9))

    bad_values = ("a ",
                  " a",
                  "  ",
                  "XX")

    def setUp(self):
        self.line = D1Line()

    def test_age_bad_value(self):
        """Raise FieldParseError if value can't be parsed to a integer"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_age(val))

    def test_age_good_values(self):
        """Parse integer from a string"""
        for input_val, output_val in self.known_values:
            self.line._parse_age(input_val)
            self.assertEqual(output_val, self.line.age)


def run_tests():
    """Execute the tests"""
    unittest.main()


if __name__ == "__main__":
    run_tests()
