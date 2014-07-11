#!/usr/bin/python
# pylint: disable=W0212, R0904

"""Unit tests for B2 Lines"""

import unittest
from ..line_formats.b_lines import B2Line
from ..line_formats import line_format_errors


class B1LineConstructor(unittest.TestCase):
    """Test Constructor for B1Line"""
    test_line = ("B2                                                         "
                 "                                   06AGL       S           "
                 "          NN")

    bad_line = ("E1F14081Reed                Laramie                         "
                "        J021100LARJREED 101902112000  9     0               "
                "           11")

    short_line = "B2ASDFASDF"

    def test_constructor_without_value(self):
        """Test constructor with no value passed"""
        line = B2Line()
        self.assertEqual((line.meet_type_1,
                          line.meet_type_2,
                          line.course_code_1,
                          line.course_code_2),
                         (None, None, None, None))

    def test_constructor_with_value(self):
        """Test constructor with line value"""
        line = B2Line(self.test_line)
        self.assertEqual((line.meet_type_1,
                          line.meet_type_2,
                          line.course_code_1,
                          line.course_code_2),
                         ("06",
                          "AG",
                          "L",
                          "S"))

    def test_constructor_short_value(self):
        """Throw InputLineError if an incorrect length line is passed"""
        self.assertRaises(line_format_errors.InputLineError,
                          lambda: B2Line(self.short_line))

    def test_constructor_bad_value(self):
        """Should throw InputLineError if the wrong line type is passed"""
        self.assertRaises(line_format_errors.InputLineError,
                          lambda: B2Line(self.bad_line))


class B2MeetType1(unittest.TestCase):
    """Test parsing meet type from string"""
    known_values = (("06", "06"),)

    bad_values = ("xx",
                  "18")

    def setUp(self):
        self.line = B2Line()

    def test_meet_type_1_bad_value(self):
        """Raise FieldParseError for invalid meet code"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_meet_type_1(val))

    def test_meet_type_1_good_values(self):
        """Parse valid meet type codes successfully"""
        for input_val, output_val in self.known_values:
            self.line._parse_meet_type_1(input_val)
            self.assertEqual(output_val, self.line.meet_type_1)

    def test_meet_type_1_no_value(self):
        """Set meet type to None if value is empty string"""
        self.line._parse_meet_type_1("  ")
        self.assertEqual(self.line.meet_type_1, None)


class B2MeetType2(unittest.TestCase):
    """Test parsing meet type from string"""
    known_values = (("08", "08"),
                    ("AG", "AG"),
                    ("ag", "AG"),
                    ("US", "US"),
                    ("us", "US"),
                    ("SR", "SR"),
                    ("sr", "SR"))

    bad_values = ("xx",
                  "18")

    def setUp(self):
        self.line = B2Line()

    def test_meet_type_2_bad_value(self):
        """Raise FieldParseError for invalid meet code"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_meet_type_2(val))

    def test_meet_type_2_good_values(self):
        """Parse valid meet tye codes successfully"""
        for input_val, output_val in self.known_values:
            self.line._parse_meet_type_2(input_val)
            self.assertEqual(output_val, self.line.meet_type_2)

    def test_meet_type_2_no_value(self):
        """Set meet type to None if value is empty string"""
        self.line._parse_meet_type_2("  ")
        self.assertEqual(self.line.meet_type_2, None)


class B2CourseCode1(unittest.TestCase):
    """Test parsing course code from string"""
    known_values = (("L", "L"),
                    ("l", "L"),
                    ("S", "S"),
                    ("s", "S"),
                    ("Y", "Y"),
                    ("y", "Y"))

    bad_values = ("x",
                  "1")

    def setUp(self):
        self.line = B2Line()

    def test_course_code_1_bad_value(self):
        """Raise FieldParseError for invalid course code"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_course_code_1(val))

    def test_course_code_1_good_values(self):
        """Parse valid course codes successfully"""
        for input_val, output_val in self.known_values:
            self.line._parse_course_code_1(input_val)
            self.assertEqual(output_val, self.line.course_code_1)

    def test_course_code_1_no_value(self):
        """Set course to None if value is empty string"""
        self.line._parse_course_code_1(" ")
        self.assertEqual(self.line.course_code_1, None)


class B2CourseCode2(unittest.TestCase):
    """Test parsing course code from string"""
    known_values = (("L", "L"),
                    ("l", "L"),
                    ("S", "S"),
                    ("s", "S"),
                    ("Y", "Y"),
                    ("y", "Y"))

    bad_values = ("x",
                  "1")

    def setUp(self):
        self.line = B2Line()

    def test_course_code_2_bad_value(self):
        """Raise FieldParseError for invalid course code"""
        for val in self.bad_values:
            self.assertRaises(line_format_errors.FieldParseError,
                              lambda: self.line._parse_course_code_2(val))

    def test_course_code_2_good_values(self):
        """Parse valid course codes successfully"""
        for input_val, output_val in self.known_values:
            self.line._parse_course_code_2(input_val)
            self.assertEqual(output_val, self.line.course_code_2)

    def test_course_code_2_no_value(self):
        """Set course to None if value is empty string"""
        self.line._parse_course_code_2(" ")
        self.assertEqual(self.line.course_code_2, None)


def run_tests():
    """Execute the tests"""
    unittest.main()


if __name__ == "__main__":
    run_tests()
