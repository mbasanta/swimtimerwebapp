#!/usr/bin/python
# pylint: disable=W0212, R0904

"""Unit tests for E1 Lines"""

import unittest
from decimal import Decimal
from ..line_formats.e1_line import E1Line
from ..line_formats import line_format_errors


class E1LineConstructor(unittest.TestCase):
    """Test Constructor for E1Line"""
    test_line = ("E1M   12BybeeMM   100E 11 12      3.50202        0Y   81.24"
                 "Y                                                          "
                 "          07")

    bad_line = ("D1F14081Reed                Laramie                         "
                "        J021100LARJREED 101902112000  9     0               "
                "        11")

    short_line = "E1ASDFASDF"

    def test_constructor_without_value(self):
        """Test constructor with no value passed"""
        line = E1Line()
        self.assertEqual((line.gender,
                          line.team_swimmer_id,
                          line.last_name,
                          line.gender1,
                          line.gender2,
                          line.distance,
                          line.stroke,
                          line.lower_age,
                          line.upper_age,
                          line.fee,
                          line.event_number,
                          line.conv_seed_time_1,
                          line.conv_seed_course_1,
                          line.seed_time_1,
                          line.seed_course_1,
                          line.conv_seed_time_2,
                          line.conv_seed_course_2,
                          line.seed_time_2,
                          line.seed_course_2),
                         (None, None, None, None, None,
                          None, None, None, None, None,
                          None, None, None, None, None,
                          None, None, None, None))

    def test_constructor_with_value(self):
        """Test constructor with line value"""
        line = E1Line(self.test_line)
        self.assertEqual((line.gender,
                          line.team_swimmer_id,
                          line.last_name,
                          line.gender1,
                          line.gender2,
                          line.distance,
                          line.stroke,
                          line.lower_age,
                          line.upper_age,
                          line.fee,
                          line.event_number,
                          line.conv_seed_time_1,
                          line.conv_seed_course_1,
                          line.seed_time_1,
                          line.seed_course_1,
                          line.conv_seed_time_2,
                          line.conv_seed_course_2,
                          line.seed_time_2,
                          line.seed_course_2),
                         ("M",
                          12,
                          "Bybee",
                          "M",
                          "M",
                          100,
                          "E",
                          11,
                          12,
                          3.5,
                          202,
                          0,
                          "Y",
                          81.24,
                          "Y",
                          None,
                          None,
                          None,
                          None))

    def test_constructor_short_value(self):
        """Throw InputLineError if an incorrect length line is passed"""
        self.assertRaises(line_format_errors.InputLineError,
                          lambda: E1Line(self.short_line))

    def test_constructor_bad_value(self):
        """Should throw InputLineError if the wrong line type is passed"""
        self.assertRaises(line_format_errors.InputLineError,
                          lambda: E1Line(self.bad_line))


class E1LineGender(unittest.TestCase):
    """Test parsing genders"""
    known_values = (("M", "M"),
                    ("m", "M"),
                    ("F", "F"),
                    ("f", "F"))

    bad_values = ("x",
                  " ")

    def setUp(self):
        self.line = E1Line()

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


class E1LineTeamSwimmerId(unittest.TestCase):
    """Test parsing team swimmer id"""
    known_values = (("    1", 1),
                    ("   21", 21),
                    ("  321", 321),
                    (" 4321", 4321),
                    ("54321", 54321))

    bad_values = ("1   1",
                  "abcde")

    def setUp(self):
        self.line = E1Line()

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


class E1LineLastName(unittest.TestCase):
    """Test parsing last name"""
    known_values = (("Smith", "Smith"),
                    ("Kim  ", "Kim"),
                    ("     ", ""))

    def setUp(self):
        self.line = E1Line()

    def test_last_name_good_values(self):
        """Strip text from string"""
        for input_val, output_val in self.known_values:
            self.line._parse_last_name(input_val)
            self.assertEqual(output_val, self.line.last_name)


class E1LineGender1(unittest.TestCase):
    """Test parsing genders"""
    known_values = (("M", "M"),
                    ("m", "M"),
                    ("F", "F"),
                    ("f", "F"))

    bad_values = ("x",
                  "1")

    def setUp(self):
        self.line = E1Line()

    def test_gender1_bad_value(self):
        """Raise FieldParseError for gender if not M/F"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_gender1(val))

    def test_gender1_good_values(self):
        """Parse M,m,F,f successfully"""
        for input_val, output_val in self.known_values:
            self.line._parse_gender1(input_val)
            self.assertEqual(output_val, self.line.gender1)

    def test_gender1_no_value(self):
        """Set gender to None if value is empty string"""
        self.line._parse_gender1(" ")
        self.assertEqual(self.line.gender1, None)


class E1LineGender2(unittest.TestCase):
    """Test parsing genders"""
    known_values = (("M", "M"),
                    ("m", "M"),
                    ("F", "F"),
                    ("f", "F"))

    bad_values = ("x",
                  "1")

    def setUp(self):
        self.line = E1Line()

    def test_gender2_bad_value(self):
        """Raise FieldParseError for gender if not M/F"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_gender2(val))

    def test_gender2_good_values(self):
        """Parse M,m,F,f successfully"""
        for input_val, output_val in self.known_values:
            self.line._parse_gender2(input_val)
            self.assertEqual(output_val, self.line.gender2)

    def test_gender2_no_value(self):
        """Set gender to None if value is empty string"""
        self.line._parse_gender2(" ")
        self.assertEqual(self.line.gender2, None)


class E1LineDistance(unittest.TestCase):
    """Test parsing distance"""
    known_values = (("  50", 50),
                    (" 100", 100),
                    (" 200", 200),
                    ("1600", 1600))

    bad_values = ("1 1 ",
                  "abcd")

    def setUp(self):
        self.line = E1Line()

    def test_distance_bad_value(self):
        """Raise FieldParseError if value can't be parsed to a integer"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_distance(val))

    def test_distance_good_values(self):
        """Parse integer from a string"""
        for input_val, output_val in self.known_values:
            self.line._parse_distance(input_val)
            self.assertEqual(output_val, self.line.distance)

    def test_distance_is_int(self):
        """Ensure distance is integer value"""
        for input_val in self.known_values:
            self.line._parse_distance(input_val[0])
            self.assertTrue(type(self.line.distance) == type(int()))

    def test_distance_no_value(self):
        """Set stroke to None if value is empty string"""
        self.line._parse_distance("    ")
        self.assertEqual(self.line.distance, None)


class E1LineStroke(unittest.TestCase):
    """Test parsing stroke codes"""
    known_values = (("A", "A"),
                    ("a", "A"),
                    ("B", "B"),
                    ("b", "B"),
                    ("C", "C"),
                    ("c", "C"),
                    ("D", "D"),
                    ("d", "D"),
                    ("E", "E"),
                    ("e", "E"))

    bad_values = ("x",
                  "1")

    def setUp(self):
        self.line = E1Line()

    def test_stroke_bad_value(self):
        """Raise FieldParseError for invalid stroke code"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_stroke(val))

    def test_stroke_good_values(self):
        """Parse valid stroke codes successfully"""
        for input_val, output_val in self.known_values:
            self.line._parse_stroke(input_val)
            self.assertEqual(output_val, self.line.stroke)

    def test_stroke_no_value(self):
        """Set stroke to None if value is empty string"""
        self.line._parse_stroke(" ")
        self.assertEqual(self.line.stroke, None)


class E1LineLowerAge(unittest.TestCase):
    """Test parsing lower swimmer age"""
    known_values = (("  1", 1),
                    (" 9 ", 9),
                    (" 21", 21),
                    ("9  ", 9),
                    ("109", 109))

    bad_values = ("a  ",
                  " a ",
                  "  a",
                  "wXX")

    def setUp(self):
        self.line = E1Line()

    def test_lower_age_bad_value(self):
        """Raise FieldParseError if value can't be parsed to a integer"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_lower_age(val))

    def test_lower_age_good_values(self):
        """Parse integer from a string"""
        for input_val, output_val in self.known_values:
            self.line._parse_lower_age(input_val)
            self.assertEqual(output_val, self.line.lower_age)

    def test_lower_age_no_value(self):
        """Set lower age to None if value is empty string"""
        self.line._parse_lower_age("   ")
        self.assertEqual(self.line.lower_age, None)

    def test_lower_age_is_int(self):
        """Ensure lower age is integer value"""
        for input_val in self.known_values:
            self.line._parse_lower_age(input_val[0])
            self.assertTrue(type(self.line.lower_age) == type(int()))


class E1LineUpperAge(unittest.TestCase):
    """Test parsing upper swimmer age"""
    known_values = (("  1", 1),
                    (" 9 ", 9),
                    (" 21", 21),
                    ("9  ", 9),
                    ("109", 109))

    bad_values = ("a  ",
                  " a ",
                  "  a",
                  "wXX")

    def setUp(self):
        self.line = E1Line()

    def test_upper_age_bad_value(self):
        """Raise FieldParseError if value can't be parsed to a integer"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_upper_age(val))

    def test_upper_age_good_values(self):
        """Parse integer from a string"""
        for input_val, output_val in self.known_values:
            self.line._parse_upper_age(input_val)
            self.assertEqual(output_val, self.line.upper_age)

    def test_upper_age_no_value(self):
        """Set upper age to None if value is empty string"""
        self.line._parse_upper_age("   ")
        self.assertEqual(self.line.upper_age, None)

    def test_upper_age_is_int(self):
        """Ensure upper age is integer value"""
        for input_val in self.known_values:
            self.line._parse_upper_age(input_val[0])
            self.assertTrue(type(self.line.upper_age) == type(int()))


class E1LineFee(unittest.TestCase):
    """Test parsing event fee"""
    known_values = (("  3.50", Decimal(3.5)),
                    (" 9    ", Decimal(9.0)),
                    (" 21.00", Decimal(21.0)),
                    ("109   ", Decimal(109.0)))

    bad_values = ("10.1.2",
                  " a    ",
                  "     a",
                  "wXXasd")

    def setUp(self):
        self.line = E1Line()

    def test_fee_bad_value(self):
        """Raise FieldParseError if value can't be parsed to a Decimal"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_fee(val))

    def test_fee_is_decimal(self):
        """Ensure fee is Decimal value"""
        for input_val in self.known_values:
            self.line._parse_fee(input_val[0])
            self.assertTrue(type(self.line.fee) == type(Decimal()))

    def test_fee_good_values(self):
        """Parse Decimal from a string"""
        for input_val, output_val in self.known_values:
            self.line._parse_fee(input_val)
            self.assertEqual(output_val, self.line.fee)

    def test_fee_no_value(self):
        """Set event fee to None if value is empty string"""
        self.line._parse_fee("      ")
        self.assertEqual(self.line.fee, None)


class E1LineEventNumber(unittest.TestCase):
    """Test parsing event number"""
    known_values = (("  1", 1),
                    (" 9 ", 9),
                    (" 21", 21),
                    ("9  ", 9),
                    ("109", 109))

    bad_values = ("a  ",
                  " a ",
                  "  a",
                  "wXX")

    def setUp(self):
        self.line = E1Line()

    def test_event_number_bad_value(self):
        """Raise FieldParseError if value can't be parsed to a integer"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_event_number(val))

    def test_event_number_is_int(self):
        """Ensure event number is Integer value"""
        for input_val in self.known_values:
            self.line._parse_event_number(input_val[0])
            self.assertTrue(type(self.line.event_number) == type(int()))

    def test_event_number_good_values(self):
        """Parse integer from a string"""
        for input_val, output_val in self.known_values:
            self.line._parse_event_number(input_val)
            self.assertEqual(output_val, self.line.event_number)

    def test_event_number_no_value(self):
        """Set event number to None if value is empty string"""
        self.line._parse_event_number("   ")
        self.assertEqual(self.line.event_number, None)


class E1LineConvSeedTime1(unittest.TestCase):
    """Test parsing seed time from string"""
    known_values = (("    3.50", 3.5),
                    (" 9.12345", 9.12345),
                    (" 21.0000", 21.0),
                    ("109.3333", 109.3333))

    bad_values = ("10.1.200",
                  " a   aa ",
                  "       a",
                  "wXXasd12")

    def setUp(self):
        self.line = E1Line()

    def test_time_bad_value(self):
        """Raise FieldParseError if value can't be parsed to a float"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_conv_seed_time_1(val))

    def test_time_good_value(self):
        """Parse float from a string"""
        for input_val, output_val in self.known_values:
            self.line._parse_conv_seed_time_1(input_val)
            self.assertEqual(output_val, self.line.conv_seed_time_1)

    def test_time_no_value(self):
        """Set seed time to None if value is empty string"""
        self.line._parse_conv_seed_time_1("       ")
        self.assertEqual(self.line.conv_seed_time_1, None)

    def test_time_is_float(self):
        """Ensure fee is float value"""
        for input_val in self.known_values:
            self.line._parse_conv_seed_time_1(input_val[0])
            self.assertTrue(type(self.line.conv_seed_time_1) == type(float()))


class E1LineConvSeedCourse1(unittest.TestCase):
    """Test parsing seed course from string"""
    known_values = (("L", "L"),
                    ("l", "L"),
                    ("S", "S"),
                    ("s", "S"),
                    ("Y", "Y"),
                    ("y", "Y"))

    bad_values = ("x",
                  "1")

    def setUp(self):
        self.line = E1Line()

    def test_course_bad_value(self):
        """Raise FieldParseError for invalid course code"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_conv_seed_course_1(val))

    def test_course_good_values(self):
        """Parse valid course codes successfully"""
        for input_val, output_val in self.known_values:
            self.line._parse_conv_seed_course_1(input_val)
            self.assertEqual(output_val, self.line.conv_seed_course_1)

    def test_course_no_value(self):
        """Set course to None if value is empty string"""
        self.line._parse_conv_seed_course_1(" ")
        self.assertEqual(self.line.conv_seed_course_1, None)


class E1LineSeedTime1(unittest.TestCase):
    """Test parsing seed time from string"""
    known_values = (("    3.50", 3.5),
                    (" 9.12345", 9.12345),
                    (" 21.0000", 21.0),
                    ("109.3333", 109.3333))

    bad_values = ("10.1.200",
                  " a   aa ",
                  "       a",
                  "wXXasd12")

    def setUp(self):
        self.line = E1Line()

    def test_time_bad_value(self):
        """Raise FieldParseError if value can't be parsed to a float"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_seed_time_1(val))

    def test_time_good_value(self):
        """Parse float from a string"""
        for input_val, output_val in self.known_values:
            self.line._parse_seed_time_1(input_val)
            self.assertEqual(output_val, self.line.seed_time_1)

    def test_time_no_value(self):
        """Set seed time to None if value is empty string"""
        self.line._parse_seed_time_1("       ")
        self.assertEqual(self.line.seed_time_1, None)

    def test_time_is_float(self):
        """Ensure fee is float value"""
        for input_val in self.known_values:
            self.line._parse_seed_time_1(input_val[0])
            self.assertTrue(type(self.line.seed_time_1) == type(float()))


class E1LineSeedCourse1(unittest.TestCase):
    """Test parsing seed course from string"""
    known_values = (("L", "L"),
                    ("l", "L"),
                    ("S", "S"),
                    ("s", "S"),
                    ("Y", "Y"),
                    ("y", "Y"))

    bad_values = ("x",
                  "1")

    def setUp(self):
        self.line = E1Line()

    def test_course_bad_value(self):
        """Raise FieldParseError for invalid course code"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_seed_course_1(val))

    def test_course_good_values(self):
        """Parse valid course codes successfully"""
        for input_val, output_val in self.known_values:
            self.line._parse_seed_course_1(input_val)
            self.assertEqual(output_val, self.line.seed_course_1)

    def test_course_no_value(self):
        """Set course to None if value is empty string"""
        self.line._parse_seed_course_1(" ")
        self.assertEqual(self.line.seed_course_1, None)


class E1LineConvSeedTime2(unittest.TestCase):
    """Test parsing seed time from string"""
    known_values = (("    3.50", 3.5),
                    (" 9.12345", 9.12345),
                    (" 21.0000", 21.0),
                    ("109.3333", 109.3333))

    bad_values = ("10.1.200",
                  " a   aa ",
                  "       a",
                  "wXXasd12")

    def setUp(self):
        self.line = E1Line()

    def test_time_bad_value(self):
        """Raise FieldParseError if value can't be parsed to a float"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_conv_seed_time_2(val))

    def test_time_good_value(self):
        """Parse float from a string"""
        for input_val, output_val in self.known_values:
            self.line._parse_conv_seed_time_2(input_val)
            self.assertEqual(output_val, self.line.conv_seed_time_2)

    def test_time_no_value(self):
        """Set seed time to None if value is empty string"""
        self.line._parse_conv_seed_time_2("       ")
        self.assertEqual(self.line.conv_seed_time_2, None)

    def test_time_is_float(self):
        """Ensure fee is float value"""
        for input_val in self.known_values:
            self.line._parse_conv_seed_time_2(input_val[0])
            self.assertTrue(type(self.line.conv_seed_time_2) == type(float()))


class E1LineConvSeedCourse2(unittest.TestCase):
    """Test parsing seed course from string"""
    known_values = (("L", "L"),
                    ("l", "L"),
                    ("S", "S"),
                    ("s", "S"),
                    ("Y", "Y"),
                    ("y", "Y"))

    bad_values = ("x",
                  "1")

    def setUp(self):
        self.line = E1Line()

    def test_course_bad_value(self):
        """Raise FieldParseError for invalid course code"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_conv_seed_course_2(val))

    def test_course_good_values(self):
        """Parse valid course codes successfully"""
        for input_val, output_val in self.known_values:
            self.line._parse_conv_seed_course_2(input_val)
            self.assertEqual(output_val, self.line.conv_seed_course_2)

    def test_course_no_value(self):
        """Set course to None if value is empty string"""
        self.line._parse_conv_seed_course_2(" ")
        self.assertEqual(self.line.conv_seed_course_2, None)


class E1LineSeedTime2(unittest.TestCase):
    """Test parsing seed time from string"""
    known_values = (("    3.50", 3.5),
                    (" 9.12345", 9.12345),
                    (" 21.0000", 21.0),
                    ("109.3333", 109.3333))

    bad_values = ("10.1.200",
                  " a   aa ",
                  "       a",
                  "wXXasd12")

    def setUp(self):
        self.line = E1Line()

    def test_time_bad_value(self):
        """Raise FieldParseError if value can't be parsed to a float"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_seed_time_2(val))

    def test_time_good_value(self):
        """Parse float from a string"""
        for input_val, output_val in self.known_values:
            self.line._parse_seed_time_2(input_val)
            self.assertEqual(output_val, self.line.seed_time_2)

    def test_time_no_value(self):
        """Set seed time to None if value is empty string"""
        self.line._parse_seed_time_2("       ")
        self.assertEqual(self.line.seed_time_2, None)

    def test_time_is_float(self):
        """Ensure fee is float value"""
        for input_val in self.known_values:
            self.line._parse_seed_time_2(input_val[0])
            self.assertTrue(type(self.line.seed_time_2) == type(float()))


class E1LineSeedCourse2(unittest.TestCase):
    """Test parsing seed course from string"""
    known_values = (("L", "L"),
                    ("l", "L"),
                    ("S", "S"),
                    ("s", "S"),
                    ("Y", "Y"),
                    ("y", "Y"))

    bad_values = ("x",
                  "1")

    def setUp(self):
        self.line = E1Line()

    def test_course_bad_value(self):
        """Raise FieldParseError for invalid course code"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_seed_course_2(val))

    def test_course_good_values(self):
        """Parse valid course codes successfully"""
        for input_val, output_val in self.known_values:
            self.line._parse_seed_course_2(input_val)
            self.assertEqual(output_val, self.line.seed_course_2)

    def test_course_no_value(self):
        """Set course to None if value is empty string"""
        self.line._parse_seed_course_2(" ")
        self.assertEqual(self.line.seed_course_2, None)


def run_tests():
    """Execute the tests"""
    unittest.main()


if __name__ == "__main__":
    run_tests()
